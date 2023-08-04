import logging


''' Задание №1
Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.
'''

# logging.basicConfig(filename='Seminar/log.log', filemode='w', encoding='utf-8', level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='Seminar/log.log', filemode='w', encoding='utf-8', level=logging.INFO)

try:
    a = 1 / 0
except ZeroDivisionError as e:
    logging.error("Ошибка деления на ноль: %s", e)
