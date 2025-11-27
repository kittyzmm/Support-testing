import math
# Класс для работы с комплексными числами
class ComplexNumber:

    # Инициализация комплексного числа
    def __init__(self, real, imaginary):
        # real: действительная часть числа
        # imaginary: мнимая часть числа
        self.real = real
        self.imaginary = imaginary

    def _check_type(self, other):
        # Проверяет, что other — экземпляр ComplexNumber
        # other: объект для проверки
        # TypeError: если other не является ComplexNumber
        if not isinstance(other, ComplexNumber):
            raise TypeError("Только комплексные числа")
    
    # Сложение двух комплексных чисел
    def __add__(self, other):        
        # Формула: (a + bi) + (c + di) = (a+c) + (b+d)i
        # Возвращает: результат сложения
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно складывать только комплексные числа")
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    # Вычитание двух комплексных чисел
    def __sub__(self, other):
        # Формула: (a + bi) - (c + di) = (a-c) + (b-d)i
        # Возвращает: результат вычитания
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно вычитать только комплексные числа")
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    # Умножение двух комплексных чисел
    def __mul__(self, other):
        # Формула: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        # Возвращает: результат умножения
        if not isinstance(other, ComplexNumber):
            raise TypeError("Можно умножать только комплексные числа")
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    # Строковое представление комплексного числа
    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"

    # Вычисляет модуль комплексного числа
    def magnitude(self):
        return math.sqrt(self.real**2 + self.imaginary**2)

# Находит комплексное число с наибольшим модулем в списке
def find_largest_magnitude(numbers_list):
    # Возвращает:
    # Число с максимальным модулем, если список не пуст
    # None, если список пуст
    
    # Если несколько чисел имеют одинаковый максимальный модуль, 
    # возвращается первое встреченное
    if not numbers_list:
        return None
    largest = numbers_list[0]
    max_magnitude = largest.magnitude()
    for num in numbers_list[1:]:
        current_magnitude = num.magnitude()
        if current_magnitude > max_magnitude:
            largest = num
            max_magnitude = current_magnitude
    return largest

def print_summary(real_part, imag_part):
    print(f"Действительная часть: {real_part}, Мнимая часть: {imag_part}")