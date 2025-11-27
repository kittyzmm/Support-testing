import unittest
from ComplexNumber import ComplexNumber, find_largest_magnitude

class TestComplexNumber(unittest.TestCase):
    # Тест на:
    # Операции сложения, вычитания, умножения
    # Вычисление модуля числа
    # Строковое представление
    # Обработка ошибок типов
    # Поиск числа с максимальным модулем

    def test_add(self):
        # Тест сложения комплексных чисел
        c1 = ComplexNumber(1, 2)
        c2 = ComplexNumber(3, 4)
        result = c1 + c2
        self.assertEqual(result.real, 4)
        self.assertEqual(result.imaginary, 6)
    
    def test_sub(self):
        # Тест вычитания комплексных чисел
        c1 = ComplexNumber(5, 6)
        c2 = ComplexNumber(2, 3)
        result = c1 - c2
        self.assertEqual(result.real, 3)
        self.assertEqual(result.imaginary, 3)
    
    def test_mul(self):
        # Тест умножения комплексных чисел
        c1 = ComplexNumber(1, 1)
        c2 = ComplexNumber(1, -1)
        result = c1 * c2
        self.assertEqual(result.real, 2)
        self.assertEqual(result.imaginary, 0)
    
    def test_magnitude(self):
        # Тест вычисления модуля комплексного числа
        c = ComplexNumber(3, 4)
        self.assertEqual(c.magnitude(), 5)
    
    def test_str(self):
        # Тест строкового представления комплексного числа
        c1 = ComplexNumber(2, 3)
        c2 = ComplexNumber(2, -3)
        self.assertEqual(str(c1), "2 + 3i")
        self.assertEqual(str(c2), "2 - 3i")
    
    def test_type_error(self):
        # Тест обработки ошибки типа при арифметических операциях
        c = ComplexNumber(1, 1)
        with self.assertRaises(TypeError):
            c + "invalid"
    
    def test_find_largest(self):
        # Тест функции поиска числа с максимальным модулем
        c1 = ComplexNumber(1, 1)
        c2 = ComplexNumber(4, 3)
        c3 = ComplexNumber(1, 0)
        result = find_largest_magnitude([c1, c2, c3])
        self.assertIs(result, c2)
    
    def test_empty_list(self):
        # Тест функции для пустого списка
        result = find_largest_magnitude([])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()