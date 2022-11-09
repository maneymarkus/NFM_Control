from absl import logging
import time

from frequency_sensor_mock import FrequencySensorMock
from frequency_controller import FrequencyController


def main():
    logging.set_verbosity(logging.DEBUG)

    f_sensor = FrequencySensorMock()
    f_controller = FrequencyController(f_sensor)
    f_controller.start(logging_level=logging.DEBUG)
    time.sleep(5)
    f_controller.stop()
    print(f_controller.queue.qsize())


if __name__ == '__main__':
    main()
