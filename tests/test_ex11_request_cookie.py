import pytest
import requests
import json

class TestRequestCookie:
    def test_request_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(response.cookies.get_dict())
        print(response.cookies.get("HomeWork"))
        expected_cookie_name = "HomeWork"
        expected_cookie_value = "hw_value"

        assert expected_cookie_name in response.cookies, f"Не удалось найти куки с именем {expected_cookie_name} в ответе"

        assert expected_cookie_value == response.cookies.get(expected_cookie_name), f"Фактическое значение cookie отличается от ожидаемого"
