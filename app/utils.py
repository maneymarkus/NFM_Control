import re
import requests


def extract_tag_content(text: str, tag_name: str) -> str:
    tag_content = None
    groups = re.search(f"<{tag_name}>(.+)</{tag_name}>", text)
    if groups is not None:
        tag_content = groups.group(1)
    return tag_content


def get_data(url: str, headers: dict) -> requests.models.Response:
    session = requests.Session()
    response = session.get(url, headers=headers, verify=False)
    return response
