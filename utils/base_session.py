import json
from json import JSONDecodeError
from requests import Session
import allure
from allure_commons.types import AttachmentType
from curlify import to_curl


class BaseSession(Session):
    def __init__(self, url):
        super(BaseSession, self).__init__()
        self.url = url

    def request(self, method, url, **kwargs):
        with allure.step(f"{method} {url}"):
            response = super().request(method, self.url + url, **kwargs)
            try:
                allure.attach(body=to_curl(response.request), name=f"Request", attachment_type=AttachmentType.TEXT,
                              extension=".txt")
                allure.attach(body=json.dumps(response.json()).encode("utf8"),
                              name=f"Response : status code is {response.status_code}",
                              attachment_type=AttachmentType.JSON,
                              extension=".json")
            except JSONDecodeError:
                allure.attach(body=response.text.encode("utf8"), name=f"Response {response.status_code}",
                              attachment_type=AttachmentType.TEXT, extension=".txt")

        return response
