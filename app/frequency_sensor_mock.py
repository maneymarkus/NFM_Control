import random


from app.frequency_sensor import FrequencySensor


class FrequencySensorMock(FrequencySensor):
    def get_current_frequency(self) -> float:
        return round(random.uniform(49.70, 50.30), 3)

    @property
    def frequency(self) -> float:
        return self.get_current_frequency()

    # alias method names
    cf = get_current_frequency
    gcf = get_current_frequency

    current_frequency = frequency
