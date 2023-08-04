import datetime
import logging


''' Задание №4
Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
'''

logging.basicConfig(
    filename='Seminar/error.log', 
    encoding='utf-8', 
    level=logging.INFO, 
    format='%(levelname)s | %(message)s'
)

def parse_date(input_text):
    current_year = datetime.datetime.now().year
    try:
        parts = input_text.split()
        day = int(parts[0].replace('-й', '').replace('-я', ''))
        weekday = parts[1]
        month_name = parts[2]
        weekdays = {
            'понедельник': 0, 'вторник': 1, 'среда': 2,
            'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6
        }
        months = {
            'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
            'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
            'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
        }
        weekday_number = weekdays[weekday]
        month_number = months[month_name]
        num_weekdays_in_month = 0
        for i in range(1, 32):
            try:
                date = datetime.datetime(current_year, month_number, i)
                if date.weekday() == weekday_number:
                    num_weekdays_in_month += 1
            except ValueError:
                break
        if day > num_weekdays_in_month:
            error_message = f"Такого дня не существует: {input_text}"
            logging.error(f"Ошибка преобразования: Входные данные - ({input_text}) | {error_message}")
            raise ValueError(error_message)
        date = datetime.datetime(current_year, month_number, 1)
        while date.weekday() != weekday_number:
            date += datetime.timedelta(days=1)
        date += datetime.timedelta(weeks=day - 1)
        return date
    except (KeyError, ValueError, IndexError):
        return None


input_texts = ["1-й четверг ноября", "3-я среда мая", "8-я пятница июля", "8-я среда декабря"]

for input_text in input_texts:
    parsed_date = parse_date(input_text)
    if parsed_date:
        print(f"Входные данные: {input_text}. Преобразованная дата: {parsed_date}")
    else:
        print(f"Входные данные: {input_text}. Ошибка преобразования. Проверь файл: error.log")
