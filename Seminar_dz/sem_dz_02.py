import logging
import sys


''' Задание
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров.
'''

# Задача с прямоугольниками

logging.basicConfig(filename='rectangle_errors.log', encoding='utf-8', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None or width == "" else width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            logging.error("Можно сложить только два прямоугольника")
            raise ValueError("Можно сложить только два прямоугольника")
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            logging.error("Можно вычесть только другой прямоугольник")
            raise ValueError("Можно вычесть только другой прямоугольник")
        new_length = self.length - other.length
        new_width = self.width - other.width
        new_length = max(new_length, 0)
        new_width = max(new_width, 0)
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            logging.error("Можно сравнивать только с другим прямоугольником")
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() < other.get_area()

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            logging.error("Можно сравнивать только с другим прямоугольником")
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            logging.error("Можно сравнивать только с другим прямоугольником")
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            logging.error("Можно сравнивать только с другим прямоугольником")
            raise ValueError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() >= other.get_area()


def get_input():
    if len(sys.argv) == 4:
        length_1 = int(sys.argv[1])
        width_1 = int(sys.argv[2])
        length_2 = int(sys.argv[3])
        width_2 = int(sys.argv[4])
    else:
        length_1 = float(input("Введите длину первого прямоугольника: "))
        width_1 = input("Введите ширину первого прямоугольника (если оставить пустым, будет считаться квадрат): ")
        if width_1:
            width_1 = float(width_1)
        length_2 = float(input("Введите длину второго прямоугольника: "))
        width_2 = input("Введите ширину второго прямоугольника (если оставить пустым, будет считаться квадрат): ")
        if width_2:
            width_2 = float(width_2)
    return length_1, width_1, length_2, width_2

def main():
    try:
        length_1, width_1, length_2, width_2 = get_input()

        rectangle_instance_1 = Rectangle(length_1, width_1)
        rectangle_instance_2 = Rectangle(length_2, width_2)

        perimeter_1 = rectangle_instance_1.get_perimeter()
        perimeter_2 = rectangle_instance_2.get_perimeter()

        sum_rectangle = rectangle_instance_1 + rectangle_instance_2
        sub_rectangle = rectangle_instance_1 - rectangle_instance_2

        print(f"Периметр первого прямоугольника: {perimeter_1}")
        print(f"Периметр второго прямоугольника: {perimeter_2}")

        sum_perimeter = sum_rectangle.get_perimeter()
        sum_area = sum_rectangle.get_area()
        print(f"Сумма периметров прямоугольников: {sum_perimeter}")
        print(f"Площадь суммы прямоугольников: {sum_area}")

        sub_perimeter = sub_rectangle.get_perimeter()
        sub_area = sub_rectangle.get_area()
        print(f"Разность периметров прямоугольников (не меньше нуля): {sub_perimeter}")
        print(f"Площадь разности прямоугольников (не меньше нуля): {sub_area}")

        if rectangle_instance_1 == rectangle_instance_2:
            print("Прямоугольники равны по площади")
        elif rectangle_instance_1 != rectangle_instance_2:
            print("Прямоугольники не равны по площади")

        if rectangle_instance_1 < rectangle_instance_2:
            print("Первый прямоугольник меньше второго по площади")
        elif rectangle_instance_1 <= rectangle_instance_2:
            print("Первый прямоугольник меньше или равен второму по площади")

        if rectangle_instance_1 > rectangle_instance_2:
            print("Первый прямоугольник больше второго по площади")
        elif rectangle_instance_1 >= rectangle_instance_2:
            print("Первый прямоугольник больше или равен второму по площади")

        with open('rectangle_info.log', 'a', encoding='utf-8') as info_file:
            info_file.write(f"Прямоугольник 1: Длина = {length_1}, Ширина = {width_1}\n")
            info_file.write(f"Прямоугольник 2: Длина = {length_2}, Ширина = {width_2}\n")
            info_file.write(f"Периметр первого прямоугольника: {perimeter_1}\n")
            info_file.write(f"Периметр второго прямоугольника: {perimeter_2}\n")
            info_file.write(f"Сумма периметров прямоугольников: {sum_perimeter}\n")
            info_file.write(f"Площадь суммы прямоугольников: {sum_area}\n")
            info_file.write(f"Разность периметров прямоугольников (не меньше нуля): {sub_perimeter}\n")
            info_file.write(f"Площадь разности прямоугольников (не меньше нуля): {sub_area}\n")

    except Exception as e:
        logging.error(f"Ошибка: {e}")
        print("роизошла ошибка. Информация в файле rectangle_errors.log")

if __name__ == "__main__":
    main()

# Запускаем код: python sem_dz_02.py 20 10 10 5
# Запускаем код: python sem_dz_01.py d f g h
