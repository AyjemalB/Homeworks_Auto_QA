import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase): # Создаём класс тестов, наследуем от unittest.TestCase

    def setUp(self):  # Метод подготовки, вызывается перед каждым тестом
        self.math = SimpleMath() # Создаём экземпляр класса SimpleMath

    def test_square_positive(self):   # Тест: квадрат положительного числа
        self.assertEqual(self.math.square(3), 9)  # Ожидаем результат 9

    def test_square_negative(self):
        self.assertEqual(self.math.square(-4), 16)

    def test_square_zero(self):
        self.assertEqual(self.math.square(0), 0)


    def test_cube_positive(self):  # Тест: куб положительного числа
        self.assertEqual(self.math.cube(2), 8) # Ожидаем результат 8

    def test_cube_negative(self):
        self.assertEqual(self.math.cube(-3), -27)

    def test_cube_zero(self):
        self.assertEqual(self.math.cube(0), 0)

if __name__ == '__main__':
    unittest.main()