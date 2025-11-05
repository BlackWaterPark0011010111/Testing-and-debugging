import unittest
from name_funk import get_form_name
print("Тест запущен") 
class NameTest(unittest.TestCase):
    """если мы создаем класс для тестирования функции
    то он должен наследоваться от класса unittest
    и должен носить имя тестируемой функции и  'TEST'."""

    def test_first_last(self):
        formatted_name=get_form_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
        
        """эта строка означает-сравни значение formatted_name со строкой  'Janis Joplin'
        assert метод проверяет соответствует ли полученный результат тому,что мы рассчитывали получить"""


    def test_first_last_middle_names(self):
        formatted_name=get_form_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')



if __name__=="__main__":
    unittest.main()