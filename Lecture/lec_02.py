import logging


######## 2. Модель logging

#### Базовые регистраторы

logging.basicConfig(level=logging.NOTSET)
logging.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logging.info('Немного информации о работе кода')
logging.warning('Внимание! Надвигается буря!')
logging.error('Поймали ошибку. Дальше только неизвестность')
logging.critical('На этом всё')
print('------------------------')


#  Функция уровня модуля logging.getLogger(name)

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

logger.debug('Очень подробная отладочная информация. Заменяем множество "принтов"')
logger.info('Немного информации о работе кода')
logger.warning('Внимание! Надвигается буря!')
logger.error('Поймали ошибку. Дальше только неизвестность')
logger.critical('На этом всё')
print('------------------------')

# Ситуация с несколькими файлами

from other import log_all

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()
