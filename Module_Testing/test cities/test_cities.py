import unittest
from city_functions import city_func
class Test(unittest.TestCase):
    def test_first_test(self):
        added_names=city_func('Paris', 'France', 5000)
        self.assertEqual(added_names, 'Paris, France 5000')

if __name__=="__main__":
    unittest.main()


""" Методы assert, предоставляемые модулем unittest
Метод Использование
assertEqual(a, b)            Проверяет, что a == b
assertNotEqual(a, b)         Проверяет, что a != b
assertTrue(x)                Проверяет, что значение x истинно
assertFalse(x)               Проверяет, что значение x ложно
assertIn(элемент, список)    Проверяет, что элемент входит в список
assertNotIn(элемент, список) Проверяет, что элемент не входит в список"""