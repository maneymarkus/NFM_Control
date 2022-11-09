from absl import logging
import multiprocessing
import time

from app.frequency_sensor import FrequencySensor


class FrequencyController:
    def __init__(self, frequency_sensor: FrequencySensor):
        self.frequency_sensor = frequency_sensor
        self.process = None
        self.queue = multiprocessing.Queue()

    def get_frequency(self):
        return self.frequency_sensor.frequency

    def get_frequency_per_second(self):
        while True:
            time.sleep(1 - time.monotonic() % 1)
            frequency = self.get_frequency()
            self.queue.put(frequency)

    def start(self):
        logging.info("Start collecting frequencies")
        self.process = multiprocessing.Process(target=self.get_frequency_per_second)
        self.process.start()

    def stop(self):
        logging.info("Stop collecting frequencies")
        self.process.terminate()
        self.process.join()
        self.process.close()
