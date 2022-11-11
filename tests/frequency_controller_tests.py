import time
import unittest

from app import FrequencySensorMock, FrequencyController


class FrequencyControllerTests(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        f_sensor_mock = FrequencySensorMock()
        self.f_controller = FrequencyController(f_sensor_mock)

    def tearDown(self) -> None:
        self.f_controller = None

    def test_get_frequency(self):
        frequency = self.f_controller.get_frequency()
        self.assertIsNotNone(frequency)
        self.assertIsInstance(frequency, float)

    def test_get_frequencies(self):
        seconds = expected_elements = 3
        self.f_controller.start()
        # add a little time padding to ensure that the function is called 5 times
        # (1 function call each second)
        time.sleep(seconds + 0.3)
        self.f_controller.stop()
        self.assertIsNotNone(self.f_controller.queue.qsize())
        self.assertEqual(expected_elements, self.f_controller.queue.qsize())
        for _ in range(self.f_controller.queue.qsize()):
            self.assertIsInstance(self.f_controller.queue.get(), float)


if __name__ == '__main__':
    unittest.main()
