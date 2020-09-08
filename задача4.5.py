# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(el_1, el):
    return el_1 * el

print(f'Список четных чисел {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов '
      f'{reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')