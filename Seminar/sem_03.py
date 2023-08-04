import logging
from datetime import datetime
import functools


''' Задание №3
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
    ○ уровень логирования,
    ○ дату события,
    ○ имя функции (не декоратора),
    ○ аргументы вызова,
    ○ результат.
'''

logger = logging.getLogger('decorator')
logger.setLevel(logging.INFO)
handler = logging.FileHandler('Seminar/decorator_2.log', encoding='utf-8')
logger.addHandler(handler)

def save_to_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        logger.info('%s | %s | %s | %s | %s', 
                    logging.getLevelName(logger.level),
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    func.__name__,
                    ', '.join(str(a) for a in args), 
                    result)
        
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
