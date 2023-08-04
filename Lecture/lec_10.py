import argparse


######## 5. Модуль argparse

#### Добавляем аргументы, add_argument

def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float, nargs=3, help='enter a b c separated by a space')
    args = parser.parse_args()
    print(quadratic_equations(*args.param))
# Запускаем код: python lec_10.py 2 -12 10
# Запускаем код: python lec_10.py -h
