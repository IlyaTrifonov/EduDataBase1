# Задание:
# Дан одномерный массив Xn. Найти произведение элементов массива, кратных 3.
# Сформировать новый массив из элементов массива Xn, значения которых меньше А.


def array_input():  # Ввод массива
    input_array = []
    # Ввод длины массива
    input_array_len = int(input("Задайте длину массива Xn: "))
    if input_array_len <= 0:
        print("Ошибка! Длина массива не положительна! Задание элементов невозможно!")
        exit()
    print("")

    # Ввод элементов массива
    print("Введите элеметы массива:")
    for i in range(input_array_len):
        input_array.append(int(input(f"Xn[{i}] = ")))
    print("")
    return input_array


def a_input():  # Ввод числа А
    print("Программа сформирует новый массив Xr из элементов массива Xn, значения которых меньше А")
    input_a_number = int(input("Введите число А: "))
    print("")
    return input_a_number


def xr_array_creation(xn_array, a_number):  # Создание нового массива Xr
    xr_array = [x for x in xn_array if x < a_number]
    if len(xr_array) != 0:
        print(f"Новый массив xr_array из элементов массива Xn, значения которых меньше {a_number}:")
        print(xr_array)
    else:
        print(f"Ошибка! Элементов, меньше {a_number} не найдено. Новый массив пуст.")
    print("")


def mult_of_tree(xn_array):  # Произведение элементов массива Xn, кратных трём
    mult_of_tree_arr = [x for x in xn_array if x % 3 == 0]
    if len(mult_of_tree_arr) > 0:
        mult_of_tree = 1
        for i in mult_of_tree_arr:
            mult_of_tree *= i
        print(f"Произведение элементов, кратных 3 равно {mult_of_tree}.")
    else:
        print("Элементов, кратных 3 нет.")


xn_array = array_input()
a_number = a_input()
xr_array_creation(xn_array, a_number)
mult_of_tree(xn_array)
