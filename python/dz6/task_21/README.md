# 21. Декораторы 1

В первом задании курса предлагается решить классическую задачу с собеседований по питону - написать декоратор, который вычисляет время выполнения оборачиваемой функции. Итак, требования к декоратору:

 - декоратор должен называться `time_decorator`
 - он должен вычислять время в секундах, в течение которого выполняется обернутая функция при ее вызове. Количество секунд должно быть выведено сразу после выполнения оборачиваемой функции. Количество секунд следует округлять до целого числа и выводить целое число
 - после оборачивания функция должна возвращать тот же результат, который возвращала исходная функция
 - пробрасывать аргументы из декоратора в функцию необязательно для выполнения этого задания

## Пример использования декоратора

```
@time_decorator
def sleep_1_sec():
    time.sleep(1)
    print("function")
    return 25

result = sleep_1_sec()
```

 > function

 > 1

`print(result)`

 > 25