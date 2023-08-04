import argparse


######## 5. Модуль argparse

parser = argparse.ArgumentParser(description='My first argument parser')

parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')

args = parser.parse_args()

print(f'В скрипт передано: {args}')

''' Примеры запуска в терминале:
python lec_07.py 42 3.14 73

# Ключ --help или -h
python lec_07.py --help

# Запуск с неверными аргументами
python lec_07.py Hello world!  # error: argument N: invalid float value: 'Hello'
'''
