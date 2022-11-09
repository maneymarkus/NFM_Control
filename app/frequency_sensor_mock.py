from absl import logging
import random


from app.frequency_sensor import FrequencySensor


class FrequencySensorMock(FrequencySensor):
    def get_current_frequency(self) -> float:
        logging.debug("get current frequency...")
        frequency = round(random.uniform(49.70, 50.30), 3)
        logging.debug(f"current frequency: {frequency}")
        return frequency

    @property
    def frequency(self) -> float:
        return self.get_current_frequency()

    # alias method names
    cf = get_current_frequency
    gcf = get_current_frequency

    current_frequency = frequency
