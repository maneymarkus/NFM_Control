import abc
import influxdb
import influxdb_client
import influxdb_client.client.write_api
import pathlib

from app import utils


class DatabaseConnection:
    def __init__(self, host: str, port: int, username: str = None, password: str = None, db_name: str = None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name

    @abc.abstractmethod
    def read(self, query):
        pass

    @abc.abstractmethod
    def write(self, data):
        pass


class InfluxDBConnection(DatabaseConnection):
    def __init__(self, host: str = "localhost", port: int = 8086):
        username = utils.get_env_value("INFLUXDB_USERNAME")
        password = utils.get_env_value("INFLUXDB_PASSWORD")
        db_name = utils.get_env_value("INFLUXDB_BUCKET")
        super().__init__(host, port, username, password, db_name)
        self.url = utils.get_env_value("INFLUXDB_USERNAME")
        self.token = utils.get_env_value("INFLUXDB_TOKEN")
        self.org = utils.get_env_value("INFLUXDB_ORGANIZATION")
        self.client = influxdb_client.InfluxDBClient(self.url, token=self.token, org=self.org)
        self.write_api = self.client.write_api(write_options=influxdb_client.client.write_api.SYNCHRONOUS)

    def write(self, point: influxdb_client.Point):
        self.write_api.write(bucket=self.db_name, org=self.org, record=point)

    def read(self, query):
        pass


if __name__ == "__main__":
    idbc = InfluxDBConnection()
    point_ex = influxdb_client.Point("measurement1").tag("tagname1", "tagvalue1").field("field1", "test")
    idbc.write(point_ex)
