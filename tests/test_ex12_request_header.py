import re

import requests

class TestRequestHeader:
    def test_request_header(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(response.headers)
        for headers in response.headers:
            print(headers)
            print(response.headers[headers])
        expected_headers = {
            "Date",
            "Content-Type",
            "Content-Length",
            "Connection",
            "Keep-Alive",
            "Server",
            "x-secret-homework-header",
            "Cache-Control",
            "Expires"
        }
        assert len(expected_headers) == len(response.headers), "Фактическое количество заголовоков отличается от ожидаемого"
        pattern = re.compile(r"[a-z]{3},\s+\d{2}\s+[a-z]{3}\s+\d{4}\s+\d{2}:\d{2}:\d{2}\s+[a-z]{3}", re.IGNORECASE)
        for header_name in expected_headers:
            assert header_name in response.headers, f"Не удалось найти заголовок с именем {header_name} в ответе"
        assert pattern.fullmatch(response.headers["Date"]), f"Значение заголовка не соответствует паттерну"
        assert response.headers["Content-Type"] == "application/json", "Фактическое значение заголовка отличается от ожидаемого"
        assert response.headers["Content-Length"] == "15", "Фактическое значение заголовка отличается от ожидаемого"
        assert response.headers["Connection"] == "keep-alive", "Фактическое значение заголовка отличается от ожидаемого"
        assert response.headers["Keep-Alive"] == "timeout=10", "Фактическое значение заголовка отличается от ожидаемого"
        assert response.headers["Server"] == "Apache", "Фактическое значение заголовка отличается от ожидаемого"
        assert response.headers["x-secret-homework-header"] == "Some secret value", "Фактическое значение заголовка отличается от ожидаемого"
        assert response.headers["Cache-Control"] == "max-age=0", "Фактическое значение заголовка отличается от ожидаемого"
        assert pattern.fullmatch(response.headers["Expires"]), f"Значение заголовка не соответствует паттерну"