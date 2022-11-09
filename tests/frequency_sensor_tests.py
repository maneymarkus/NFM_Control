import unittest

from app.frequency_sensor import FrequencySensor


class FrequencySensorTests(unittest.TestCase):
    def setUp(self) -> None:
        super(FrequencySensorTests, self).setUp()
        self.f_sensor = FrequencySensor()

    def tearDown(self) -> None:
        self.f_sensor = None

    def test_url(self):
        self.assertIsNotNone(self.f_sensor.url)
        self.assertIsInstance(self.f_sensor.url, str)

    def test_collect_data(self):
        data = self.f_sensor.collect_data()
        self.assertIsNotNone(data)

    def test_get_current_frequency(self):
        frequency = self.f_sensor.frequency
        self.assertIsNotNone(frequency)
        self.assertIsInstance(frequency, float)


if __name__ == '__main__':
    unittest.main()
