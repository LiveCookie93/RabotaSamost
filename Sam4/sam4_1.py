from datetime import  datetime
# импорт из библиотеки datetime модуля datetime
from math import sqrt
# импорт из библиотеки math модуля sqrt


def main(**kwargs):
    # создание функции с аргументом **kwargs
    for key in kwargs.items():
        # цикл for in
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # создание переменной и вычисление ее пораметров
        print(result)
        # вывести в консоль результат вычисления переменной


if __name__ == "__main__":
    # проверка запускаем ли мы основной файл
    start_time = datetime.now()
    # создание переменной с использывание библиотеки
    main(
        # запуск функции
        one=[10,3],
        two=[5,4],
        three=[15,13],
        # значение аргументов функции
    )
    time_costs = datetime.now() - start_time
    # определение времени выполнения программы
    print(f'Время выполнения программы - {time_costs}')
    # вывод в консоль сколько времени потраченно на выполнение команды