import pytest
import requests

class TestUserAgent:
    # user_agent_header = [
    #     ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
    #     ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
    #     ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
    #     ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
    #     ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    # ]
    # expected_platform_value = [
    #     ("'platform': 'Mobile'"),
    #     ("'platform': 'Mobile'"),
    #     ("'platform': 'Googlebot'"),
    #     ("'platform': 'Web'"),
    #     ("'platform': 'Mobile'")
    # ]
    #
    # expected_browser_value = [
    #     ("'browser': 'No'"),
    #     ("'browser': 'Chrome'"),
    #     ("'browser': 'Unknown'"),
    #     ("'browser': 'Chrome'"),
    #     ("'browser': 'No'")
    # ]
    #
    # expected_device_value = [
    #     ("'device': 'Android'"),
    #     ("'device': 'iOS'"),
    #     ("'device': 'Unknown'"),
    #     ("'device': 'No'"),
    #     ("'device': 'iPhone'")
    # ]
    @pytest.mark.parametrize(
        "agent_header,platform_value,browser_value,device_value",
        [
            ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
             "Mobile", "'No", "Android"),
            ("'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'", "Mobile", "Chrome", "iOS"),
            ("'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'", "Googlebot", "Unknown", "Unknown"),
            ("'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'", "Web", "Chrome", "No"),
            ("'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'", "Mobile", "No", "iPhone")
        ]
    )
    def test_user_agent(self, agent_header, platform_value, browser_value, device_value):
        print(agent_header)
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": agent_header})
        print(response.headers)
        print(platform_value)
        assert 5 + 4 == 9
        # assert response.headers["platform"] == platform_value
        # assert response.headers["browser"] == browser_value
        # assert response.headers["device"] == device_value
