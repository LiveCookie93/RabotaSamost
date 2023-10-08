# Напишите функцию tpl_sort(), которая сортирует кортеж, состоящий из целых чисел
# по возрастанию и возвращает его. Если хотя бы один элемент не является целым
# числом, то функция возвращает исходный кортеж.


def tpl_sort(tpl):
    for i in tpl:
        if not isinstance(i, int):
            return tpl
    return tuple(sorted(tpl))


# Тесты
print(tpl_sort((5, 5, 3, 1, 9)))
print(tpl_sort((5, 5, 2.1, '1', 9)))
print(tpl_sort((5, 12, 4, 1, 9)))
