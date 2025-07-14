# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number
# і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
import logging
from pathlib import Path
import xml.etree.ElementTree as ET

current_directory = Path.cwd()
new_path = current_directory / "folder_xml"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.getLogger('').addHandler(console_handler)

def find_group_number():
    for file in new_path.iterdir():
        if file.is_file() and file.suffix == ".xml":
            print(f"Читаємо файл: {file.name}")
            tree = ET.parse(file)
            root = tree.getroot()
            for group in root.findall('group'):
                if group is not None:
                    number = group.find('number')
                    if number is not None:
                        logging.info(f"Group: {group.find('name').text}, number: {number.text}")
                    else:
                        print(f"Group: {group.find('name').text}, number: Не знайдено")

find_group_number()