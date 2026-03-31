from typing import List


"""
Задача № 1.
Используя filter() и lambda, отфильтруйте из списка
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] только нечетные числа.
"""

list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = list(map(int, filter(lambda x: x % 2, list_nums)))


"""
Задача № 2.
Напишите функцию apply_operations(numbers, *operations), к
оторая принимает список чисел и произвольное количество lambda-функций, 
последовательно применяя каждую ко всему списку.
"""

def apply_operations(numbers: List, *operations: callable) -> List:
    new_list = []
    for func in operations:
        new_list.append(list(map(func, numbers)))
    
    return new_list

# print(apply_operations([1, 2, 3], lambda x: x + 1, lambda x: x + 2))  ->  [[2, 3, 4], [3, 4, 5]]



"""
Задача № 3.
Напишите генератор chunked(lst, size), который разбивает список на куски заданного размера 
и поочередно их выдает. Например, chunked([1,2,3,4,5], 2) → [1,2], [3,4], [5].
"""

def chunked(lst: list, size: int) -> List:
    return [lst[i:i + size] for i in range(0, len(lst), size)]


# print(chunked([1,2,3,4,5], 2))  ->  [[1, 2], [3, 4], [5]]


"""
Задача № 4.
Напишите генератор prime_numbers(), который бесконечно генерирует простые числа. 
Выведите первые 20.
"""

def prime_numbers(n: int) -> int:
    
    for i in range(1, n + 1):
        yield i

# print(*prime_numbers(20))


"""
Задача № 5.
Напишите функцию safe_convert(value, type_func), 
которая пытается преобразовать value 
с помощью переданной функции (например, int, float).
При ошибке возвращает None.
"""

def safe_convert(value: any, type_func: callable) -> any:
    try:
        return type_func(value)
    except (ValueError, TypeError):
        return None

# print(safe_convert('3', int))


"""
Задача № 6.
Создайте собственный класс исключения NegativeNumberError. 
Напишите функцию sqrt_safe(n), которая считает квадратный корень из числа, 
но при отрицательном n выбрасывает NegativeNumberError с понятным сообщением.
"""

class NegativeNumberError(Exception):
    pass



def sqrt_safe(n: int) -> any:
    try:
        if n < 0:
            raise NegativeNumberError(f"Невозможно вычесть коень из отрицательного числа")
        else:
            return n ** 0.5
    except NegativeNumberError as e:
        return f"Ошибка: {e}"

# print(sqrt_safe(9))
# print(sqrt_safe(-9))


"""
Задача № 7.
Напишите функцию-калькулятор calculator(a, b, op), 
где op — строка ("+", "-", "*", "/").
Обработайте все возможные исключения: деление на ноль, неизвестная операция, некорректные типы аргументов.
"""

def calculator(a: float|int, b: float|int, op: str) -> int|float:
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Деление на ноль невозможно")
            else:
                return a / b
        else:
            raise ValueError(f"Неизвестная операция: '{op}'. Допустимые операции: '+', '-', '*', '/'")
    except ZeroDivisionError as e:
        return f"Ошибка: {e}"
    except TypeError as e:
        return f"Ошибка: {e}"
    except ValueError as e:
        return f"Ошибка: {e}"


# print(calculator(0, 0, '/'))
# print(calculator(1, 4, ')'))
# print(calculator('1', 4, '+'))
