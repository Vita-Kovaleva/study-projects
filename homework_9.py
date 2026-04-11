import math
from dataclasses import dataclass


"""Задача №1.
Создай класс Circle с protected атрибутом _radius.
Добавь @property для radius (с проверкой: радиус > 0), 
и вычисляемые свойства area и perimeter через @property - 
они должны пересчитываться автоматически при изменении радиуса."""

class Circle:
    def __init__(self, radius):
        self._radius = None
        self.radius = radius


    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Радиус должен быть больше 0")
        self._radius = value

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius


"""Задача №2.
Создай класс Vector с атрибутами x и y. 
Реализуй магические методы __add__ (сложение двух векторов), 
__str__ (вывод в формате "Vector(x, y)"), и __eq__ (сравнение). 
Проверь: Vector(1, 2) + Vector(3, 4) должен давать Vector(4, 6)."""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Можно складывать только векторы")
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y


"""Задача №3.
Создай класс Temperature с @property для celsius, fahrenheit и kelvin. 
При установке значения через любое свойство должны автоматически пересчитываться остальные. 
Хранить следует только одно внутреннее значение."""


class Temperature:
    def __init__(self):
        self._kelvin = 0

    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self._kelvin = value + 273.15

    @property
    def fahrenheit(self):
        return (self._kelvin - 273.15) * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._kelvin = (value - 32) * 5/9 + 273.15

    @property
    def kelvin(self):
        return self._kelvin

    @kelvin.setter
    def kelvin(self, value):
        if value < 0:
            raise ValueError("Температура в Кельвинах не может быть отрицательной")
        self._kelvin = value



"""Задача №4.
Используй @dataclass для создания класса Point с полями x: float и y: float. 
Добавь метод distance_to(other: Point) - расстояние до другой точки. 
Затем создай дочерний @dataclass класс Point3D, добавив поле z: float, и переопредели distance_to."""


@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

@dataclass
class Point3D(Point):
    z: float

    def distance_to(self, other: 'Point3D') -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )

"""Задача №5.
Создай класс-итератор Countdown, который при итерации возвращает числа от start до 0. 
Реализуй __iter__ и __next__ (при исчерпании бросай StopIteration). П
роверь в цикле for и через list()."""

class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        self.current = self.start 
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
