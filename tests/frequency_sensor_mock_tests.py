import unittest

from app.frequency_sensor_mock import FrequencySensorMock


class FrequencySensorMockTests(unittest.TestCase):
    def setUp(self) -> None:
        super(FrequencySensorMockTests, self).setUp()
        self.f_sensor_mock = FrequencySensorMock()

    def tearDown(self) -> None:
        self.f_sensor_mock = None

    def test_get_current_frequency(self):
        frequency = self.f_sensor_mock.frequency
        self.assertIsNotNone(frequency)
        self.assertIsInstance(frequency, float)


if __name__ == '__main__':
    unittest.main()
