from typing import List
import string


def read_lines(filename: str) -> List[str]: 
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.readlines()
    except Exception as e:
        raise Exception(f"Произошла ошибка при чтении файла '{filename}': {e}")
    
    return text



def write_lines(filename: str, lines: List[str]) -> None: 
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(f'{line}\n')  # '/n' - для новой строки
    except Exception as e:
        raise Exception(f"Произошла ошибка при записи файла '{filename}': {e}")
    
    print("Текст успешно записан в файл")


def count_words(filename: str) -> dict: 

    """
    считает сколько раз каждое слово встречается в файле 
    и возвращает словарь
    """

    counter_of_words = dict()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.read()

            translator = str.maketrans('', '', string.punctuation)
            cleaned_line = lines.translate(translator).lower()

            words = cleaned_line.split()
            
            for word in words:
                counter_of_words[word] = counter_of_words.get(word, 0) + 1
    except Exception as e:
        raise Exception(f"Произошла ошибка при подсчёте слов файла '{filename}': {e}")
    print(counter_of_words)
    
    return counter_of_words

    

