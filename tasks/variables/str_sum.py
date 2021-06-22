"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Функция str_sum принимает 2 строки, которые содержат целые числа.
Отредактировать функцию так, чтобы она возвращала целое значение - сумму чисел
в строках

ПРИМЕРЫ
--------------------------------------------------------------------------------
str_sum("4", "5") -> 9
str_sum("34", "5") -> 39
"""


def str_sum(str1: str, str2: str) -> int:
    """
    Возвращает сумму чисел в двух строках

    :param str1: первое число
    :type str1: str

    :param str2: второе число
    :type str2: str

    :return: сумму чисел из строк
    :rtype: int
    """
    result = None
    return result


if __name__ == '__main__':
    str1_val = input('Введите первое число: ')
    str2_val = input('Введите второе число: ')
    print(f'Сумма чисел: {str_sum(str1_val, str2_val)}')