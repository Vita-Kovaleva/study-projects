
"""
Задача №1
Привести к целому типу - 1.6, 2.99

"""

num_1: int = int(-1.6)
num_2: int = int(2.99)




"""
Задача №2
Заменить символ "#" на символ "/ в строке 'www.my_site.com#about'

"""

txt: str = 'www.my_site.com#about'

#1 вариант
new_txt: str = ''
new_txt: str = txt.replace('#', '/')


#2 вариант
new_txt_2 = ''
for i in txt:
    if i == '#':
        new_txt_2 += '/'
    else:
        new_txt_2 += i




"""
Задача №3
Напишите программу, которая добавляет 'ing' к слову stroka

"""

stroka = 'stroka'
stroka += 'ing'




"""
Задача №4
В строке "Ivanou Ivan" поменяйте местами слова => "Ivan Ivanou" 

"""

full_name = "Ivanou Ivan"

#1 вариант
rename = full_name[7:] + ' ' + full_name[:6]

#2 вариант
full_name = tuple(full_name.split())
surname, name = full_name
new_name = ' '.join([name, surname])




"""
Задача №5
Напишите программу которая удаляет пробел в начале, в конце строки

"""

text = ' пробелы в начале и в конце '

#1 вариант
new_txt_without_space = text.strip()

#2 вариант
new_str = text
while new_str.startswith(' '):
    new_str = new_str[1:]
while new_str.endswith(' '):
    new_str = new_str[:-1]




"""
Задача №6
Создайте словарь, связав его с переменной school, 
и наполните его данными которые бы отражали количество 
учащихся в десяти разных классах (например, 1а, 1б, 2б, ба, 7в и т.д.)

"""

school = {'1a':21, '1б':22, '2б':19, '3а':20, '3б':23, 
          '4а':18, '5а':17, 'ба':22, '7а':23, '7в':20}




"""
Задача №7
Создайте список и извлеките из него списка второй элемент.

"""

my_list = 'Создайте список и извлеките из него списка второй элемент'.split()
second_elem_from_list = my_list[1]




"""
Задача №8
Вывести входит ли строка 1 в строку2 (пример: employ и employment)

"""

string_1 = 'employ'
string_2 = 'employment'

result = string_1 in string_2




"""
Задача №9
Вывести нужные символы
x= "My name is Agent Smith" print(x[?]) #y
print(x[?:?:?]) #nesgt

"""

x = "My name is Agent Smith"
#print(x[1])
#print(x[3:16:3])




"""
Задача №10
Есть массив чисел. Известно, что каждое число в этом массиве имеет пару, 
кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
Напишите программу, которая будет выводить уникальное число

"""

massive = [1, 5, 2, 9, 2, 9, 1]

for i in massive:
    if massive.count(i) % 2 != 0:
        print(i)
