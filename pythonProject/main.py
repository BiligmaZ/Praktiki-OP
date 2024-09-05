"""Добавление модуля математических функций и констант"""

import math

# Вычисление сверхзолотого сечения
q = (2 + ((116 + (12 * math.sqrt(93))) ** (1/3)) +
     ((116 - (12 * math.sqrt(93))) ** (1/3))) / 6
b = 1 - q

def get_nth_number(number):
    """Вычисление n-го числа последовательности"""
    return round((q ** number - b ** number) / math.sqrt(5))

def is_in_sequence(num):
    """Определение, является ли число элементом последовательности"""
    for i in range(1, 1000):
        if get_nth_number(i) == num:
            return i
    return -1

def check(string):
    """Проверка входных данных"""
    try:
        float(string)
        return "Y"
    except ValueError:
        return "N"

# Запрос ввода и вывод результата
while True:
    n = input("Введите наутральное целое число n (для выхода введите 'q'): ")
    if n == 'q':
        break
    if check(n) == "N":
        print('Ошибка ввода. Нужно ввести число.')
    elif not n.isdigit():
        print('Ошибка ввода. Введите целое число.')
    else:
        n = int(n)
        nth_number = get_nth_number(n)
        print("n-е число последовательности:", nth_number)
        in_sequence = is_in_sequence(n)
        if in_sequence != -1:
            print("Число", n, "является", in_sequence,
                  "-м элементом последовательности.")
        else:
            print("Число", n, "не является элементом последовательности.")
        print()
