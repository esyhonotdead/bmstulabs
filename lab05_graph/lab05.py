"""
Пысларь Никита, ИУ7-11Б
Лабораторная работа #4, Вариант - 24
Задание:
1) Написать программу для вывода значения функции в таблицу (вводные данные: начальное и конечное значение аругмента, шаг разбиения аргумента)
2) Построить график одной из функций
"""

import math


def result_table():
    """
    Функция рисует таблицу
    """
    # Заголовок таблицы
    header = f"| {'Аргумент':^10} | {'Функция #1':^15} | {'Функция #2':^15} | {'Функция #3':^15} |"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    # Смешное вычисление
    for x in [x / 100 for x in range(0, 105, 5)]:
        func_1 = math.pow(2, x) - 4 * x
        func_2 = math.pow(x, 3) - 3 * math.pow(x, 2) + 1
        func_3 = (func_1 + func_2) / 10
        print(f"| {x:^10} | {func_1:^15.5g} | {func_2:^15.5g} | {func_3:^15.5g} |")
    print("-" * len(header))


def result_graph():
    """
    График функции который я уже ненавижу
    """
    # Уже знаете
    for x in [x / 100 for x in range(0, 105, 5)]:
        func_1 = math.pow(2, x) - 4 * x
        func_2 = math.pow(x, 3) - 3 * math.pow(x, 2) + 1
        func_3 = (func_1 + func_2) / 10
    # TODO
    # Второе задание заставит плакать любого кодера


result_table()


