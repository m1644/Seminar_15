import logging
import sys


''' Задание
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров.
'''

# Задача с факториалом

logging.basicConfig(filename='factorial_errors.log', encoding='utf-8', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class FactorialGenerator:
    def __init__(self, start=1, stop=None, step=1):
        self.start = start
        self.stop = stop if stop is not None else start
        self.step = step

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def generate_factorials(self):
        current = self.start
        while current <= self.stop:
            yield self.factorial(current)
            current += self.step


def get_input():
    if len(sys.argv) == 3:
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
        step = int(sys.argv[3])
    else:
        args = input("Введите три параметра через пробел (start stop step): ").split()
        start = int(args[0]) if len(args) >= 1 else 1
        stop = int(args[1]) if len(args) >= 2 else None
        step = int(args[2]) if len(args) >= 3 else 1
    return start, stop, step

def main():
    try:
        start, stop, step = get_input()
        generator = FactorialGenerator(start, stop, step)
        for factorial in generator.generate_factorials():
            print(f"Факториал {start}: {factorial}")
            start += step
        with open('factorial_info.log', 'a', encoding='utf-8') as info_file:
            info_file.write(f"Параметры: start = {start}, stop = {stop}, step = {step}\n")
            for n in range(start, stop + 1, step):
                factorial = generator.factorial(n)
                info_file.write(f"Факториал {n}: {factorial}\n")
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        print("Произошла ошибка. Информация в файле factorial_errors.log")


if __name__ == "__main__":
    main()

# Запускаем код: python sem_dz_01.py 1 4 1
# Запускаем код: python sem_dz_01.py f g h
