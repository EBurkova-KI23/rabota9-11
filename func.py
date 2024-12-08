import random
from concurrent.futures import ThreadPoolExecutor
import time


def rot90(matrix):
    """
    Поворачивает матрицу на 90 градусов против часовой стрелки.

    :param matrix: Исходная матрица.
    :return: Повернутая матрица.
    """
    return [list(reversed(col)) for col in zip(*matrix)]


def rot270(matrix):
    """
    Поворачивает матрицу на 90 градусов по часовой стрелке.

    :param matrix: Исходная матрица.
    :return: Повернутая матрица.
    """

    return [list(row) for row in list(zip(*matrix))[::-1]]


def big_sum(mas_a, mas_b):
    """
    Вычисляет сумму двух массивов, представляющих большие числа.

    :param mas_a: Первый массив.
    :param mas_b: Второй массив.
    :return: Массив, представляющий сумму двух больших чисел.
    """
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a + int_mas_b
    mas_x = []
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    mas_x.reverse()
    return mas_x


def big_diff(mas_a, mas_b):
    """
    Вычисляет разность двух массивов, представляющих большие числа.

    :param mas_a: Первый массив.
    :param mas_b: Второй массив.
    :return: Массив, представляющий разность двух больших чисел.
    """
    int_mas_a = int(''.join(map(str, mas_a)))
    int_mas_b = int(''.join(map(str, mas_b)))
    x = int_mas_a - int_mas_b
    mas_x = []
    minus = 0
    if x < 0:
        x = abs(x)
        minus = 1
    while x > 0:
        mas_x.append(x % 10)
        x //= 10
    mas_x.reverse()
    if minus:
        mas_x[0] = mas_x[0] * (-1)
    return mas_x


def how_much_same(mas_a, mas_b):
    """
    Подсчитывает количество одинаковых элементов в двух массивах.

    :param mas_a: Первый массив.
    :param mas_b: Второй массив.
    :return: Количество одинаковых элементов.
    """
    k = 0
    for i in range(len(mas_a)):
        a = abs(mas_a[i])
        for j in range(len(mas_b)):
            b = abs(mas_b[j])
            if a == b:
                k += 1
    return k


def get_arr(lenght):
    """
    Получает массив от пользователя.

    :param lenght: Длина массива.
    :return: Массив, введенный пользователем.
    """
    a = []
    for i in range(lenght):
        a.append(int(input()))
    return a


def gen_arr(lenght):
    """
    Генерирует случайный массив.

    :param lenght: Длина массива.
    :return: Случайный массив.
    """
    a = []
    for i in range(lenght):
        a.append(random.randint(0, 9))
    time.sleep(random.randint(1, 10))
    return a


def get_matrix(lenght, wight):
    """
    Получает матрицу от пользователя.

    :param lenght: Длина матрицы.
    :param wight: Ширина матрицы.
    :return: Матрица, введенная пользователем.
    """
    a = []
    for i in range(lenght):
        b = []
        for j in range(wight):
            b.append(int(input()))
        a.append(b)
    return a


def gen_matrix(lenght, wight):
    """
    Генерирует случайную матрицу.

    :param lenght: Длина матрицы.
    :param wight: Ширина матрицы.
    :return: Случайная матрица.
    """
    a = []
    for i in range(lenght):
        b = []
        for j in range(wight):
            b.append(random.randint(0, 9))
        a.append(b)
    return a


def gen_or_get_mas():
    """
    Запрашивает у пользователя, хочет ли он ввести массив вручную или сгенерировать его случайно.

    :return: Массив, введенный пользователем или сгенерированный случайно.
    """
    print("Желаете ввести массив в ручную? y/n \n В случае отказа массив будет сгенерирован случайно")
    ch = input()
    if ch == 'y':
        print("Введите длинну массива")
        lenght = int(input())
        return get_arr(lenght)
    elif ch == 'n':
        print("Введите длинну массива")
        lenght = int(input())
        with ThreadPoolExecutor() as executor:
            a = executor.submit(gen_arr, lenght).result()
            b = executor.submit(gen_arr, lenght).result()
            c = executor.submit(gen_arr, lenght).result()
            print("Матрица a " , a)
            print("Матрица b " , b)
            print("Матрица c " , c)
            print("Вывберите понравившуюся матрицу a, b или c")
            char = input()
            if char == 'a':
                return a
            if char == 'b':
                return b
            if char == 'c':
                return c
    else:
        print("Неверные данные")


def gen_or_get_mat():
    """
    Запрашивает у пользователя, хочет ли он ввести матрицу вручную или сгенерировать её случайно.

    :return: Матрица, введенная пользователем или сгенерированная случайно.
    """
    print("Желаете ввести матрицу в ручную? y/n \n В случае отказа матрица будет сгенерирована случайно")
    ch = input()
    if ch == 'y':
        print("Введите длинну матрицы")
        lenght = int(input())
        print("Введите ширину матрицы")
        width = int(input())
        return get_matrix(lenght, width)
    elif ch == 'n':
        print("Введите длинну матрицы")
        lenght = int(input())
        print("Введите ширину матрицы")
        width = int(input())
        return gen_matrix(lenght, width)
    else:
        print("Неверные данные")