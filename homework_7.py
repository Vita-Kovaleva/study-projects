import warnings
from functools import wraps
from typing import Callable


"""
Задача № 1.
Напишите рекурсивную функцию palindrome(s), которая проверяет, 
является ли строка палиндромом. Без срезов и reversed(), только рекурсия.
"""

def palindrome(s: str) -> bool:
    str_low = s.lower()
    
    if len(str_low) <= 1:
        return True
    
    if str_low[0] != str_low[-1]:
        return False
        
    return palindrome(str_low[1:-1])


# print(palindrome("Шалаш"))
# print(palindrome("дом"))


"""
Задача № 2.
Напишите функцию make_validator(min_val, max_val), 
которая возвращает функцию-валидатор. 
Валидатор принимает число и возвращает True если оно в диапазоне, иначе False.
"""

def make_validator(min_val: int, max_val: int) -> callable:
    def valid(num: int) -> bool:
        return min_val <= num <= max_val
    return valid

try:
    print("Ведите 2 числа для задания диапазона")
    min_n, max_n = int(input("Введите левую границу: ")), int(input("Введите правую границу: "))
    validator = make_validator(min_n, max_n)
    # print(f"Ваше число находится в диапазоне от {min_n} от {max_n}" if validator(int(input("Введите число для проверки: "))) 
    #   else f"Ваше число не находится в диапазоне от {min_n} от {max_n}")

except ValueError as v_er:
    print(f"Ошибка типа: {v_er}")


"""
Задача № 3.
Напишите декоратор @retry(n), 
который при возникновении любого исключения повторяет вызов функции до n раз. 
Если все попытки провалились — пробрасывает последнее исключение.
"""

def retry(n: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Callable:
            last_ex = None
            for _ in range(n):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
            raise last_ex
        return wrapper
    return decorator



"""
Задача № 4.
Напишите декоратор @deprecated(message), 
который выводит предупреждение при вызове функции (через warnings.warn) и всё равно выполняет её. 
Сохраняйте метаданные через functools.wraps.
"""

def deprecated(message: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(message, category=DeprecationWarning)
            return func(*args, **kwargs)
        return wrapper
    return decorator


"""
Задача № 5.
Напишите рекурсивную функцию binary_search(lst, target) (бинарный поиск числа в списке), 
оберните её декоратором @logger, который логирует каждый вызов с параметрами.
"""

import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с аргументами: lst={args[0]}, target={args[1]}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} вернула: {result}")
        return result
    return wrapper

@logger
def binary_search(lst, target, left=0, right=None):
    if right is None:
        right = len(lst) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return binary_search(lst, target, left, mid - 1)
    else:
        return binary_search(lst, target, mid + 1, right)
