import pytest
import requests
import json

class TestRequestCookie:
    def test_request_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies)