import datetime as dt
import time



def time_decorator(function):
    def wrapper():
        time_1 = dt.datetime.now()
        res = function()
        time_2 = (dt.datetime.now() - time_1).total_seconds()
        print(round(time_2))
        return res
    return wrapper


if __name__ == '__main__':
    @time_decorator
    def sleep_1_sec():
        time.sleep(1)
        print('function')
        return 25
result = sleep_1_sec()
print(result)