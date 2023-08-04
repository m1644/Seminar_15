import argparse


######## 5. Модуль argparse

# Создаём парсер, ArgumentParser
'''
● prog — заменяет название файла в первой строке справки на переданное имя,
● description — описание в начале справки
● epilog — описание в конце справки
'''

parser = argparse.ArgumentParser(
    prog='average', 
    description='My first argument parser', 
    epilog='Returns the arithmetic mean'
)

parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'В скрипт передана: {args}')
# Запускаем код: python lec_08.py --help
