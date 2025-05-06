"""
Обработать N случайных целых чисел в диапазоне [-26;13].
Отсортировать числа по убыванию, найти количество отрицательных чисел. N вводит пользователь, программа выводит N чисел на экран
"""

from calc import rand_n
from check_input import check_num


def input_num(str_for_input: str) -> int:
    num = input(str_for_input)
    if check_num(num):
        result = int(num)
    else:
        print("Вы ввели не число, повторите ввод \n")
        result = input_num(str_for_input)

    return result


def main():

    print("Программа обрабатывает N случайных целых чисел в диапазоне [-26;13]")
    flag = True
    while flag:
        flag = True
        while flag:
            n_int = input_num("Введите количество N случайных чисел: ")
            if n_int > 0 and n_int != float("inf"):
                flag = False
            elif n_int <= 0:
                print("Введите число больше")
            else:
                print("Вы ввели слишком большое число")

    result_neg, result_num = rand_n(n_int)

    print(f"Количество отрицательных чисел: {result_neg}")
    print(f"Отсортированный список случайных чисел: {result_num}")


    flag = True
    while flag:
        dalsh = input("Для продолжения работы введите 1, для выхода 0: ")
        if dalsh == "1":
            flag = False
            main()
        elif dalsh != "0":
            print("Не верный ввод")
        else:
            flag = False


if __name__ == '__main__':
    main()