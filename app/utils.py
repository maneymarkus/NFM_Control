import dotenv
import pathlib
import re
import requests


ENV_PATH = pathlib.Path(__file__).parent.parent.joinpath(".env")


def extract_tag_content(text: str, tag_name: str) -> str:
    """
    Extract the value of a tag with a given `tag_name` in a given `text`.
    Most applicable to xml data

    :param text:
    :param tag_name:
    :return:
    """
    tag_content = None
    groups = re.search(f"<{tag_name}>(.+)</{tag_name}>", text)
    if groups is not None:
        tag_content = groups.group(1)
    return tag_content


def get_data(url: str, headers: dict) -> requests.models.Response:
    """
    Send a http request to the given `url` with the given `headers` and return the response

    :param url:
    :param headers:
    :return:
    """
    session = requests.Session()
    response = session.get(url, headers=headers, verify=False)
    return response


def get_env_value(key: str, env_path: pathlib.Path = ENV_PATH):
    """
    Get value of an environment variable according to the given `key` from the .env file at
    the given `env_path` (or the default path, if none is given)

    :param key:
    :param env_path:
    :return:
    """
    env_values = dotenv.dotenv_values(env_path)
    value = env_values[key]
    return value
