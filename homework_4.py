"""
Задача 1. 
Напиши код который выведет таблицу умножения до 10 на N (введенное с клавиатуры) в таком формате
  3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27
"""

n = int(input("Введите число для таблицы умножения: "))

for i in range(1, 11):
    print(n * i, end=' | ')


"""
Задача 2.
Попроси пользователя ввести имя и возраст. Выведи фразу: «Через 10 лет тебе будет <X> лет, <ИМЯ>!»
"""

age = int(input("Введите ваш возраст: "))
name = input("Введите ваше имя: ")

print(f"Через 10 лет тебе будет {age + 10} лет, {name}!")


"""
Задача 3.
Даны два списка цен в долларах и курс валюты. Используй map чтобы перевести все цены в рубли. 
Затем используй zip чтобы создать словарь {товар: цена_в_рублях}:

items = ['хлеб', 'молоко', 'кофе']
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2
"""

items = ['хлеб', 'молоко', 'кофе']
prices_usd = [1.5, 2.0, 8.0]
rate = 3.2


def kurs(n):
    return n * rate

prices_rub = list(map(kurs, prices_usd))  # prices_rub = list(map(lambda n: n * rate, prices_usd)) - вариант без отдельной функции
items_with_price = dict(zip(items, prices_rub))


"""
Задача 4.
Напиши функцию fizzbuzz(n) которая принимает число и возвращает строку: 
'Fizz' если делится на 3, 
'Buzz' если делится на 5, 
'FizzBuzz' если делится на оба, иначе само число в виде строки. 
Вызови её для чисел от 1 до 20 через map.
"""

def fizzbuzz(n):
    flag = ''
    if n % 3 == 0:
        if n % 5 == 0:
            flag = 'FizzBuzz'
        else:
            flag = 'Fizz'
    elif n % 5 == 0:
        flag = 'Buzz'

    return flag if flag else n

print(*(map(fizzbuzz, range(1, 21))), sep='\n')


"""
Задача 5.
Напиши функцию *args с именем my_stats которая принимает любое количество чисел 
и возвращает сразу три значения — минимум, максимум и среднее. 
"""

def my_stats(*args):
    min_num = min(args)
    max_num = max(args)
    medium = (sum(args) / len(args))

    return min_num, max_num, medium

# print(*(my_stats(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))


"""
Задача 6.
Напиши функцию build_profile(**kwargs) которая принимает любые именованные аргументы 
и возвращает словарь с этими данными 
плюс автоматически добавляет ключ 'registered': True. 
Добавь к функции docstring.
"""

def build_profile(**kwargs):

    """Эта функция принимает любые именованные аргументы 
    и возвращает словарь с этими данными,
    а так же автоматически добавляет ключ 'registered': True."""

    build_prof = kwargs
    build_prof['registered'] = True

    return build_prof

# print(build_profile(name = 'Name', age = 20))
# Вывод: {'name': 'Name', 'age': 20, 'registered': True}


"""
Задача 7.
Создай модуль math_utils.py с тремя функциями: square(n) — возводит в квадрат, 
cube(n) — возводит в куб, is_even(n) — возвращает True/False.
В main.py импортируй модуль, попроси пользователя ввести число через input, 
примени все три функции и выведи результаты. Защити вызовы конструкцией if __name__ == "__main__"."""

import math_utils

n_math = int(input("Введите число: "))

if __name__ == "__main__":
    print(f"Куб числа {n_math} равен: {math_utils.cube(n_math)},\n"
          f"Квадрат числа {n_math} равен: {math_utils.square(n_math)}," 
          f"Является ли число чётным: {math_utils.is_even(n_math)}")
