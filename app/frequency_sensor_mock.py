from absl import logging
import random


from app.frequency_sensor import FrequencySensor


class FrequencySensorMock(FrequencySensor):
    """
    This class mocks the FrequencySensor class for testing purposes and overwrites only the
    "critical" method(s)
    """
    def get_current_frequency(self) -> float:
        """
        Overwrite method in original class and return random (but still reasonable) frequency

        :return:
        """
        logging.debug("get current frequency...")
        frequency = round(random.uniform(49.70, 50.30), 3)
        logging.debug(f"current frequency: {frequency}")
        return frequency
