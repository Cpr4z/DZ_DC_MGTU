import re


class Field(dict):
    _valid_key_pattern = re.compile("^(([a-zA-z]\d+)|(\d+[a-zA-Z]))")

    @classmethod
    def _is_key_valid(cls, key):
        """Метод провяет является ли ключ подходящим, то есть совпадает ли с регуляркой"""
        if cls._valid_key_pattern.fullmatch(key):
            return True
        return False

    @staticmethod
    def _normalise_key(key):
        """Метод проверяет подходит ли ключ по условиям типа данных и длины и приводит его к нормальному виду"""
        if not (isinstance(key, str), isinstance(key, tuple)) or (isinstance(key, tuple) and len(key) > 2):
            raise TypeError
        return ''.join(sorted(tuple(map(str, key)))).lower()

    def _aplly_field_key_rules(method):
        def wrap(self, key, *args, **kwargs):
            key = self._normalise_key(key)
            if not self._is_key_valid(key):
                raise ValueError
            return method(self, key, *args, **kwargs)
        return wrap

    @_aplly_field_key_rules
    def __getitem__(self, key):
        return super().__getitem__(key)

    @_aplly_field_key_rules
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    @_aplly_field_key_rules
    def __delitem__(self, key):
        return super().__delitem__(key)

    @_aplly_field_key_rules
    def __contains__(self, key):
        return super().__contains__(self._normalise_key(key))

    @_aplly_field_key_rules
    def __missing__(self, key):
        return None

    def __iter__(self):
        return super().values().__iter__()
