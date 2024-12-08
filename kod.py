from concurrent.futures import ThreadPoolExecutor
import func
import sys

def menu(point):
    """
    Основное меню программы.

    :param point: Пункт меню, выбранный пользователем.
    """
    if point == 1:
        mas_a = func.gen_or_get_mas()
        mas_b = func.gen_or_get_mas()
        print("Сумма (1) или разность (2)")
        x = int(input())
        if x == 1:
            print(func.big_sum(mas_a, mas_b))
        elif x == 2:
            print(func.big_diff(mas_a, mas_b))
        else:
            print("Error")
    elif point == 2:
        with ThreadPoolExecutor() as executor:
            a = executor.submit(func.gen_or_get_mat)
            mat = a.result()
        print("Повернуть матрицу на право (1) или на лево (2)")
        x = int(input())
        if x == 1:
            print(func.rot90(mat))
        elif x == 2:
            print(func.rot270(mat))
        else:
            print("Error")
    elif point == 3:
        mas_a = func.gen_or_get_mas()
        mas_b = func.gen_or_get_mas()
        print(func.how_much_same(mas_a, mas_b))
    elif point == 4:
        print("Завершение работы программы.") 
        sys.exit()
    else:
        print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1) 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов.")
        print("2) Vатрица N на M. Требуется повернуть матрицу на 90 градусов против часовой или по часовой.")
        print("3) 2 массива с цифрами, каждый представляет собой большое число. Нужно произвести сумму или разность массивов.")
        print("0) Завершение работы")
        print("Выберите пункт меню: ")
        menu(int(input()))