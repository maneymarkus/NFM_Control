from absl import logging

from app import utils


class FrequencySensor:
    url = "https://netzfrequenzmessung.de:9080/frequenz02.xml"

    def collect_data(self):
        """
        Send a http request to `self.url` and return the received response

        :return:
        """
        headers = {
            "content-type": "text/plain"
        }

        response = utils.get_data(self.url, headers)
        return response

    def get_current_frequency(self) -> float:
        """
        Retrieves the current frequency from self.url.
        The data is retrieved in the XML format and looks like this:
        <r>
        <f2>50.009</f2>
        <n>C_298</n>
        <z> 09.11.2022 16:55:51</z>
        <p>252.1</p>
        <d>007</d>
        <dt>-10,57</dt>
        </r>

        :return:
        """

        logging.debug("get current frequency...")
        response = self.collect_data()
        response_body = response.text

        frequency = float(utils.extract_tag_content(response_body, "f2"))
        logging.debug(f"current frequency: {frequency}")
        return frequency

    @property
    def frequency(self) -> float:
        """
        Class property to get current frequency for convenience reasons

        :return:
        """
        return self.get_current_frequency()

    # alias method names
    cf = frequency
    gcf = frequency
    current_frequency = frequency
