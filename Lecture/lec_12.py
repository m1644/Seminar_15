import argparse


######## 5. Модуль argparse

# Параметр action для аргумента

parser = argparse.ArgumentParser(description='Sample')
parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int, dest='types')
parser.add_argument('-f', action='append_const', const=float, dest='types')
parser.add_argument('-s', action='append_const', const=str, dest='types')
args = parser.parse_args()
print(args)
# Запускаем код: python lec_12.py -h
# Запускаем код: python lec_12.py -x -y -z 42 -z 73 -i -f -s
