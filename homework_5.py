"""
Задача№ 1.
Напиши функцию copy_file(source: str, destination: str) -> bool 
которая читает содержимое файла source и записывает его в destination. 
Возвращает True если успешно. Проверь что файл-копия создался.
"""

def copy_file(source: str, destination: str) -> None:
    data = source.read()
    destination.write(data)

with open('source.txt', 'r') as source, open('destination.txt', 'w') as destination:
    copy_file(source, destination)



"""
Задача№ 2. 
Создай файл grades.txt где каждая строка содержит имя студента и его оценку через запятую:
Анна,85
Иван,72
Петр,91
Напиши код который читает файл и добавляет в конец каждой строки статус: 'отлично' 
если оценка >= 90, 'хорошо' если >= 75, иначе 'удовлетворительно'. 
Сохрани результат в новый файл grades_with_status.txt.
"""

def add_grade(grade: int) -> str:

    """
    - 'отлично' — оценка >= 90
    - 'хорошо' — оценка >= 75
    - 'удовлетворительно' — в остальных случаях
    """

    if grade >= 90:
        return 'отлично'
    elif 90 > grade >= 70:
        return 'хорошо'
    else:
        return 'удовлетворительно'


with open('grades.txt', 'r', encoding='utf-8') as grades, \
open('grades_with_status.txt', 'w', encoding='utf-8') as grades_with_status:
    lines = grades.readlines()

    for line in lines:
        line = line.strip()

        name, grade_str = line.split(',')
        grade = int(grade_str)
        
        new_line = f'{name} - {add_grade(grade)}\n'
        grades_with_status.write(new_line)


"""
Задача№ 3.
Напиши функцию age_calculator(birth_date_str: str) -> int 
которая принимает дату рождения в формате 'dd/mm/yyyy' (input)  и возвращает полных лет. 
"""

from datetime import datetime

def age_calculator(birth_date_str: str) -> int:
    date_now = datetime.today()
    birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")

    age = date_now.year - birth_date.year

    if (date_now.month, date_now.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age


date_input = input("Введите дату рождения (dd/mm/yyyy): ")
print(f"Полных лет: {age_calculator(date_input)}")


"""
Задача№ 4.
Напиши модуль file_utils.py с тремя полностью аннотированными функциями:
def read_lines(filename): ...
def write_lines(filename, lines): ...
def count_words(filename): ... # count_words считает 
сколько раз каждое слово встречается в файле и возвращает словарь. 
В main.py импортируй и протестируй все три.
"""

import file_utils

text = ['Привет, это тестовый файл для провекрки.', 
        'Для проверки запишем этот текст в файл',
        'Затем проверим какое количество слов есть в файле',
        'Текст для проверки']

if __name__ == "__main__":
    file_utils.write_lines('test_file.txt', text)
    print(file_utils.read_lines('test_file.txt'))
    file_utils.count_words('test_file.txt')


"""
Задача№ 5.
Напиши функцию password_checker(correct_password) 
которая возвращает вложенную функцию check(password). 
Вложенная принимает пароль и возвращает True если совпадает, иначе False.
"""

from typing import Callable


def password_checker(correct_password: str) -> Callable:
    def check(password: str) -> bool:
        return password == correct_password
    return check

validate_pasw = password_checker("secret123")

print(validate_pasw("secret123"))  # True
print(validate_pasw("sicret123"))  # False
