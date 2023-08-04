import time
from collections import namedtuple
from datetime import datetime


######## 04. Пара полезных структур данных

#### Модуль collections

# Фабричная функция namedtuple

User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))

print(u_1)
print(f'{type(User)}, {type(u_1)}')
print('------------------------')


# Точечная нотация

User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))

print(u_1)
print(u_1.first_name, u_1.birthday.year)
print('------------------------')


# Задержка

SECONDS = 4

User = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')

print(f'Пауза в {SECONDS} секунд...')

time.sleep(SECONDS)

u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')
print('------------------------')


# Метод _replace

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
a = Point(2, 3, 4)
b = a._replace(z=0, x=a.x + 4)
print(b)
print('------------------------')


# Экземпляры можно сортировать

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
data = [Point(2, 3, 4), Point(10, -100, -500), Point(3, 7, 11),
Point(2, 202, 1)]
print(sorted(data))
print('------------------------')


# Экземпляр может быть ключом словаря, элементом множества и т.п.

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
}
print(d)

mut_point = Point(2, [3, 4, 5], 6)
print(mut_point)
# d.update({mut_point: 'bad_point'}) # TypeError: unhashable type: 'list'
print('------------------------')


# Модуль array

from array import array, typecodes

byte_array = array('B', (1, 2, 3, 255))
print(byte_array)
print(typecodes)
print('------------------------')


# Массивы поддерживают методы списка list

long_array = array('l', [-6000, 800, 100500])
long_array.append(42)
print(long_array)
print(long_array[2])
print(long_array.pop())
print('------------------------')

''' Защита
long_array = array('l', [-6000, 800, 100500])
long_array.append(2**32) # OverflowError: Python int too large to convert to C long
long_array.append(3.14) # TypeError: 'float' object cannot be interpreted as an integer
'''

''' Задание
Перед вами несколько строк кода. 
Напишите что выведет программа, не запуская код. 
У вас 3 минуты.
'''

Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics', 'genetics'], defaults=[5, 5, 5, 5])
d = {
    'Ivanov': Data(4, 5, 3, 5),
    'Petrov': Data(physics=4, genetics=3),
    'Sidorov': Data(),
}
print(d)

''' Ответ:
{'Ivanov': Data(mathematics=4, chemistry=5, physics=3, genetics=5), 
 'Petrov': Data(mathematics=5, chemistry=5, physics=4, genetics=3), 
 'Sidorov': Data(mathematics=5, chemistry=5, physics=5, genetics=5)}
'''
