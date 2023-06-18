def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = (f'Привет, {name}! Тебе {age} лет.')
    print(f'\n{output}')
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = (a+b)*2
    assert perimeter == 60
    # TODO сосчитайте площадь
    area = a*b
    assert area == 200


def test_circle():
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    import math
    r = 23
    a = math.pi
    # TODO сосчитайте площадь

    area = a * math.pow(r,2)
    assert area == 1661.9025137490005
    # TODO сосчитайте длину окружности
    length = a * (r*2)
    assert length == 144.51326206513048
    print(f'\nРадиус: {area}, \nДлина: {length}')


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """
    # TODO создайте список
    import random

    l = [random.randint(1, 100) for _ in range(10)]
    l.sort()
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    for int in l:
        if l.count(int) > 1:
            l.remove(int)
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))
    print('\nЗначения:', *d.values())
    assert isinstance(d, dict)
    assert len(d) == 5