import json

import requests
import time

# 1) создавал задачу
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

token = response.json()["token"]
time_sleep = response.json()["seconds"]
print(token)
# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":"" + token + ""})
if response.json()["status"] != "Job is NOT ready":
    print("Статус неверный!")
else:
    print("Статус верный!")

# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
time.sleep(time_sleep)

# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":"" + token + ""})
if response.json()["status"] != "Job is ready":
    print("Статус неверный!")
else:
    print("Статус верный!")
obj = json.loads(response.content)

if "result" in obj:
    print("Поле 'result' присутствует в ответе")
else:
    print("Поле 'result' отсутствует в ответе")