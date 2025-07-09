# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

from pathlib import Path
import json
import logging

current_directory = Path.cwd()
print("Поточна робоча директорія:", current_directory)

LOG_FILE = "json__Karabut.log"
log_path = current_directory / "json__Karabut.log"

logger = logging.getLogger("json_validation")
logger.setLevel(logging.ERROR)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def json_validation():
    new_path = current_directory / "folder_json"
    print("Нова робоча директорія:", new_path)
    for item in new_path.iterdir():
        if item.is_file() and item.suffix == ".json":
            print("Знайдено:", item.name)
        try:
            with open(item, 'r', encoding='utf-8') as file:
                data = json.load(file)
                print(data)
        except json.JSONDecodeError as e:
            logger.error(f"Файл {item.name}. Помилка розбору JSON:, {e}")
            print("Помилка розбору JSON:", e)
        except FileNotFoundError:
            logger.error(f"Файл {item.name} не знайдено")
            print("Файл не знайдено")
        except PermissionError:
            logger.error(f"Немає прав доступу до файлу {item.name}")
            print("Немає прав доступу до файлу")

json_validation()