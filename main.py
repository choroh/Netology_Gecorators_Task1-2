"""
Netology. Derarators.

1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы,
   с которыми вызвалась и возвращаемое значение.
2. Написать декоратор из п.1, но с параметром – путь к логам.
3. Применить написанный логгер к приложению из любого предыдущего д/з.
"""
from datetime import datetime
a, b = 3, 5
path = 'files/log.txt'


def decorator(func):
    """
    Функция декоратор принимает другую функцию,принимает путь для записи лога, записывает в файл дату и
    время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
    :param func:
    :return:
    """
    info = {}

    def wrapper(file_path_, *args):
        '''
        Декоратор
        :param file_path_:
        :param args:
        :return:
        '''
        date_time = datetime.now().strftime("%d %b %Y, %H : %M : %S")
        result = func(file_path_, *args)
        #  Обертка принимает функцию для обработки
        info['Дата и время вызова функции: '] = date_time
        info['Имя функции: '] = func.__name__
        info['Аргументы функции: '] = args
        info['Файл лога: '] = result[0]
        info['Возвращаемое значение: '] = result[1]
        with open(file_path_, 'a', encoding="UTF-8") as f:
            for key, value in info.items():
                f.write(f'{key} {value}\n')
        print(f'Данные функции {func.__name__} записаны в файл {file_path_}')
        return result
        #  Обертка возвращает результат работы принятой функции
    return wrapper


@decorator
def multiply(path_, a_, b_):
    m = a * b
    return path_, m


multiply(path, a, b)
