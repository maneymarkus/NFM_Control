import requests
import unittest

from app import utils


class MyTestCase(unittest.TestCase):
    def test_extract_tag_content(self):
        expected_tag_content = "expected"
        text = f"askljdhkjl<f>{expected_tag_content}</f>alksjdfhjkl"
        tag_name = "f"
        actual_tag_content = utils.extract_tag_content(text, tag_name)
        self.assertIsNotNone(actual_tag_content)
        self.assertIsInstance(actual_tag_content, str)
        self.assertEqual(expected_tag_content, actual_tag_content)
        tag_name_2 = "d"
        actual_tag_content_2 = utils.extract_tag_content(text, tag_name_2)
        self.assertIsNone(actual_tag_content_2)

    def test_get_data(self):
        url = "https://google.com"
        headers = {
            "content-type": "text/plain"
        }
        data = utils.get_data(url, headers)
        self.assertIsNotNone(data)
        self.assertIsInstance(data, requests.models.Response)


if __name__ == '__main__':
    unittest.main()
