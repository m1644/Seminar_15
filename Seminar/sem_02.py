import functools
import logging


''' Задание №2
На семинаре про декораторы был создан логирующий декоратор. 
Он сохранял аргументы функции и результат её работы в файл.
Напишите аналогичный декоратор, но внутри используйте модуль logging.
'''

logger = logging.getLogger('decorator') 
logger.setLevel(logging.INFO)
handler = logging.FileHandler('Seminar/decorator_1.log', encoding='utf-8') 
logger.addHandler(handler)

def save_to_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info("Вызвана функция %s с аргументами %s и ключевыми аргументами %s. Результат: %s",
                    func.__name__, args, kwargs, result)
        return result
    return wrapper

@save_to_log
def function_plus(a, b, c):
    return a + b + c

@save_to_log
def greet(name):
    return f"Hello, {name}!"

function_plus(2, 3, 4)
function_plus(10, 20, 30)
greet('Max') 
greet('John')
