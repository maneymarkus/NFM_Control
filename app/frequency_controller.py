from absl import logging
import multiprocessing
import time

from app.frequency_sensor import FrequencySensor


class FrequencyController:
    def __init__(self, frequency_sensor: FrequencySensor):
        """
        Initialize Frequency controller

        :param frequency_sensor:
        """
        self.frequency_sensor = frequency_sensor
        self.process = None
        self.queue = multiprocessing.Queue()

    def get_frequency(self):
        """
        Return current "measured" frequency from frequency sensor

        :return:
        """
        return self.frequency_sensor.frequency

    def get_frequency_per_second(self, logging_level=logging.INFO):
        """
        Starts an infinite time loop to get the "measured" frequency from the frequency sensor
        each second

        :param logging_level:
        :return:
        """
        logging.set_verbosity(logging_level)
        while True:
            time.sleep(1 - time.monotonic() % 1)
            frequency = self.get_frequency()
            self.queue.put(frequency)

    def start(self, logging_level=logging.INFO):
        """
        Start a separate process to let this controller run concurrently and infinitely

        :param logging_level:
        :return:
        """
        if self.process is None:
            logging.info("Start collecting frequencies")
            self.process = multiprocessing.Process(
                target=self.get_frequency_per_second,
                args=(logging_level, )
            )
            self.process.start()

    def stop(self):
        """
        Stop the separate process and therefore also the monitoring of the frequency sensor

        :return:
        """
        if self.process is not None and self.process.is_alive():
            logging.info("Stop collecting frequencies")
            self.process.terminate()
            self.process.join()
            self.process.close()
            self.process = None
