import re
import requests
import time


def main():
    url = "https://netzfrequenzmessung.de:9080/frequenz01.xml"
    headers = {
        "content-type": "text/plain"
    }

    frequency_time_series = []

    while True:
        time.sleep(1 - time.monotonic() % 1)
        response = get_data(url, headers)
        response_body = response.text

        frequency = float(extract_tag_content(response_body, "f"))
        print(frequency)
        frequency_time_series.append(frequency)


def get_data(url: str, headers: dict) -> requests.models.Response:
    session = requests.Session()
    response = session.get(url, headers=headers, verify=False)
    return response


def extract_tag_content(text: str, tag_name: str) -> str:
    tag_content = re.search(f"<{tag_name}>(.+)</{tag_name}>", text).group(1)
    return tag_content


if __name__ == '__main__':
    main()
