# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

from pathlib import Path
import csv

current_directory = Path.cwd()
print("Поточна робоча директорія:", current_directory)
new_path = current_directory / "folder_csv"
print("Нова робоча директорія:", new_path)
output_file = current_directory / "results_Karabut.csv"


def save_unique_lines_from_csv_files():
    unique_lines = set()
    for file in new_path.iterdir():
        if file.is_file() and file.suffix == ".csv":
            print(f"Читаємо файл: {file.name}")
            with open(file, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    unique_lines.add(tuple(row))
    print(f"Знайдено унікальних рядків: {len(unique_lines)}")
    print(unique_lines)

    with open(output_file, mode = 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in unique_lines:
            writer.writerow(row)

    print(f"Всі знайдені унікальні рядки збережено в {output_file}")



save_unique_lines_from_csv_files()
