"""Задача №1.
Создай класс Library с атрибутом класса books = [] и методами add_book(title), remove_book(title) и show_books(). 
Продемонстрируй, что список книг общий для всех объектов класса."""

class Library:
    books = []  

    def add_book(self, title: str):
        self.books.append(title)

    def remove_book(self, title: str):
        if title in self.books:
            self.books.remove(title)

    def show_books(self):
        print(f"Книги в библиотеке: {self.books}")


lib_1 = Library()
lib_2 = Library()

lib_1.add_book("'1984' Дж. Озуэл")
lib_2.add_book("'Мы' Е.И. Замятин")



"""Задача №2.
Создай иерархию: базовый класс Employee с атрибутами name и salary, методом get_info().
Дочерние классы Manager (добавляет department) и Developer (добавляет language).
Каждый переопределяет get_info()."""

class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Manager: {self.name}, salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name: str, salary: int, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        return (f"Manager: {self.name}, salary: {self.salary}, "
                f"department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def get_info(self):
        return (f"Developer: {self.name}, salary: {self.salary}, "
                f"language: {self.language}")


"""Задача №3.
Реализуй класс Stack (стек) с протектед атрибутом _items = [] 
и методами push(item), pop(), peek() (посмотреть верхний элемент), is_empty() и size()."""

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item: int):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Размер стека: {stack.size()}")
print(f"Верхний элемент: {stack.peek()}")
print(f"Извлечён: {stack.pop()}")
print(f"Is stack empty? {stack.is_empty()}")


"""Задача №4.
Создай класс Vehicle с методом move(), выводящим "Moving...". 
Создай дочерние классы Car, Boat и Plane, каждый переопределяет move() по-своему. 
Напиши функцию start_journey(vehicle), которая вызывает move() 
у любого переданного транспорта - продемонстрируй полиморфизм."""

class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Едет")

class Boat(Vehicle):
    def move(self):
        print("Плывёт")

class Plane(Vehicle):
    def move(self):
        print("Летит")

def start_journey(vehicle):
    vehicle.move()


car = Car()
boat = Boat()
plane = Plane()

start_journey(car)
start_journey(boat)
start_journey(plane)


"""Задача №5.
Создай класс Student с атрибутами name и grades (список оценок).
Добавь методы add_grade(grade), average() (средняя оценка), highest() и lowest().
Защити grades через одиночное подчёркивание."""

class Student:
    def __init__(self, name):
        self.name = name
        self._grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self._grades.append(grade)
        else:
            print("Оценка должна быть от 1 до 5")

    def average(self):
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)

    def highest(self):
        return max(self._grades) if self._grades else None

    def lowest(self):
        return min(self._grades) if self._grades else None


student = Student("Алексей")
student.add_grade(4)
student.add_grade(5)
student.add_grade(3)

print(f"Средняя оценка: {student.average()}")
print(f"Высшая оценка: {student.highest()}")
print(f"Низшая оценка: {student.lowest()}")
