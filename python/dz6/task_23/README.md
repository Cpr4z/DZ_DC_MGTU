# 23. Сеть

## Задание

[Здесь](https://jsonplaceholder.typicode.com/) описано некоторое API, в котором есть доступ к базе пользователей, постов, комментариев и т.д. Методы, которые мы будем использовать, описаны в разделе Resources. Примеры использования API (правда, на JavaScript'е) описаны на том же сайте по ссылке [Guide](https://jsonplaceholder.typicode.com/guide/). Вам нужно для каждого пользователя посчитать количество оставленных постов и количество оставленных комментариев. Всю информацию для этого нужно стягивать GET-запросами по API. Результат нужно отправить в ваше пространство в https://webhook.site в виде POST-запроса, содержащего JSON следующего формата:

```
  "statistics": [
    {
      "id": 1,
      "username": "lolkek",
      "email": "user1@mail.dot",
      "posts": 125,
      "comments": 1358
    },
    {
      "id": 2,
      "username": "cheburek",
      "email": "user2@mail.dot",
      "posts": 5,
      "comments": 12
    }
  ]
}
```

Поскольку среда исполнения Яндекс-контеста не имеет доступа к интернету, проверить правильность выполнения задания вы можете, отправив в качестве ответа на задание "Сеть" `pickle` объекта ответа запроса:

```
response = requests.post(.....)

with open("solution.pickle", 'wb') as f:
    pickle.dump(response, "solution.py")
```

И отправляйте тот файл, который появится в результате исполнения этого кода.