import os
import sys
import logging
from collections import namedtuple


''' Задание №6
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
    ○ имя файла без расширения или название каталога,
    ○ расширение, если это файл,
    ○ флаг каталога,
    ○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
'''

logging.basicConfig(
    filename='directory_info.log', 
    encoding='utf-8', 
    level=logging.INFO, 
    format='%(levelname)s | %(message)s'
)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_dir'])

def collect_directory_info(directory_path):
    try:
        if not os.path.exists(directory_path):
            logging.error(f"Directory does not exist: {directory_path}")
            return

        items = os.listdir(directory_path)
        info_list = []

        for item in items:
            full_path = os.path.join(directory_path, item)
            is_directory = os.path.isdir(full_path)
            
            name, extension = os.path.splitext(item)
            parent_dir = os.path.basename(directory_path)
            
            info = FileInfo(name=name, extension=extension if not is_directory else '', 
                            is_directory=is_directory, parent_dir=parent_dir)
            info_list.append(info)
            
            logging.info(f"Name: {info.name}, Extension: {info.extension}, Is Directory: {info.is_directory}, Parent Dir: {info.parent_dir}")
        
        return info_list
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python ыуь_06.py <directory_path>")
        return
    
    directory_path = sys.argv[1]
    info_list = collect_directory_info(directory_path)
    
    if info_list:
        print("Directory information collected and logged. Check directory_info.log for details.")
    else:
        print("Error occurred. Check directory_info.log for details.")

if __name__ == "__main__":
    main()

# Запускаем код: python sem_06.py .
