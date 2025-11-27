import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

print(f"Количество редиректов от изначальной точки назначения до итоговой: {len(response.history)}")

print(f"Итоговый URL: {response.url}")