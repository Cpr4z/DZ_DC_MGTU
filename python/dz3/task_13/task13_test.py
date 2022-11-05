from task13 import check_num as phone, check_email as email
import unittest


class CheckSringTest(unittest.TestCase):
    """Класс, тестирующий функцию check_string"""

    def test_check_num_good(self):
        """Функция тестирующая номера телефонов"""
        self.assertEqual(phone('89160000000'), True)
        self.assertEqual(phone('+79160000000'), True)
        self.assertEqual(phone('9160000000'), True)
        self.assertEqual(phone('8(916)000-00-00'), True)
        self.assertEqual(phone('+7(916)000-00-00'), True)
        self.assertEqual(phone('(916)000-00-00'), True)
        self.assertEqual(phone('8 (916) 000-00-00'), True)
        self.assertEqual(phone('+7 (916) 000-00-00'), True)
        self.assertEqual(phone('(916) 000-00-00'), True)
        self.assertEqual(phone('8(916)0000000'), True)
        self.assertEqual(phone('+7(916)0000000'), True)
        self.assertEqual(phone('(916)0000000'), True)
        self.assertEqual(phone('8-916-000-00-00'), True)
        self.assertEqual(phone('+7-916-000-00-00'), True)
        self.assertEqual(phone('916-000-00-00'), True)

    def test_check_num_bad(self):

        self.assertEqual(phone('694524242'), False)
        self.assertEqual(phone('aqeqeqlkq'), False)
        self.assertEqual(phone('-424242434'), False)
        self.assertEqual(phone('89014542424224'), False)


    def test_check_email_good(self):
        """Функция тестирующая адреса почты"""
        self.assertEqual(email('abc@abc.ab'), True)
        self.assertEqual(email('abc@abc.ab.ab'), True)
        self.assertEqual(email('a@ab.ab'), True)
        self.assertEqual(email('abc.abc@abc.abc'), True)

    def test_check_email_bad(self):
        self.assertEqual(email('@abc.abc'), False)
        self.assertEqual(email('abc@abc'), False)
        self.assertEqual(email('abc@abc.a'), False)
        self.assertEqual(email('abc@abc.abc.a'), False)
        self.assertEqual(email('abc@abc.'), False)
        self.assertEqual(email('abc@abc@abc'), False)

if __name__ == '__main__':
    unittest.main()
