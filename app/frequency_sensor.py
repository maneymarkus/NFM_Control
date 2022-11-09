import app.utils as utils


class FrequencySensor:
    url = "https://netzfrequenzmessung.de:9080/frequenz02.xml"

    def collect_data(self):
        headers = {
            "content-type": "text/plain"
        }

        response = utils.get_data(self.url, headers)
        return response

    def get_current_frequency(self) -> float:
        response = self.collect_data()
        response_body = response.text

        frequency = float(utils.extract_tag_content(response_body, "f2"))
        return frequency

    @property
    def frequency(self) -> float:
        return self.get_current_frequency()

    # alias method names
    cf = get_current_frequency
    gcf = get_current_frequency

    current_frequency = frequency
