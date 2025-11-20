import requests

# Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
#
# Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE
#
# При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос. Например, если вы делаете GET-запрос,
# параметр method должен равняться строке ‘GET’. Если POST-запросом - то параметр method должен равняться ‘POST’.  И так далее.
#
# Надо написать скрипт, который делает следующее:
#
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.

response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_post.text)

response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_get.text)

response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_put.text)

response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_delete.text)



# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response_head = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method":"HEAD"})
print(response_head.text)
print(response_head.status_code)
response_head = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_head.text)
print(response_head.status_code)

# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method":"POST"})
print(response_post.text)

response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method":"GET"})
print(response_get.text)

response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method":"PUT"})
print(response_put.text)

response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method":"DELETE"})
print(response_delete.text)

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса.
# Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот,
# когда типы совпадают, но сервер считает, что это не так.
allowed_methods = ["GET", "POST", "PUT", "DELETE"]
for method in allowed_methods:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={f"method":"" + method + ""})
    print(f"Метод GET с параметром {method} выводит значение {response.text}")

    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"" + method + ""})
    print(f"Метод POST с параметром {method} выводит значение {response.text}")

    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"" + method + ""})
    print(f"Метод PUT с параметром {method} выводит значение {response.text}")

    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"" + method + ""})
    print(f"Метод DELETE с параметром {method} выводит значение {response.text}")

    print("------------------------------------------------------------------------------------")