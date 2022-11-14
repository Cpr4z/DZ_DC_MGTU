class Calculator:
    """Класс калькулятора"""
    last = None
    def __init__(self):
        self._log = []

    def __log_operation(method):
        def shell(self, a, b, *args, **kwargs):
            answer = method(self, a, b, *args, **kwargs)
            self.__class__.last = f'{method.__name__}({a}, {b}) == {answer}'
            self._log.append(self.last)
            return answer
        return shell

    @__log_operation
    def sum(self, a, b):
        return a+b

    @__log_operation
    def sub(self, a, b):
        return a-b

    @__log_operation
    def mul(self, a, b):
        return a*b

    @__log_operation
    def div(self, a, b, mod=False):
        return a%b if mod else a/b

    def history(self, n):
        if len(self._log) < n:
            return None
        else: return self._log[-n]

    @classmethod
    def clear(cls):
        cls.last=None
