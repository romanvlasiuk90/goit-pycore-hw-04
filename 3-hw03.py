from pathlib import Path
import sys
from colorama import Fore

def viz_dir_struct(path):
    try:
        # Перевірка чи існує шлях
        if not Path(path).exists():
            raise FileNotFoundError
        print(Fore.WHITE + "****************")
        print(f"{Fore.BLUE}📂 {Path(path).name}")
        # Обходимо підпапки та файли
        for item in Path(path).iterdir():
            # Папки
            if item.is_dir():
                print(f"{Fore.MAGENTA} ┣ 📂 {item.name}")
            # Файли
            elif item.is_file():
                print(f"{Fore.GREEN} ┣ 📜 {item.name}")
        print(Fore.WHITE + "****************")
    except FileNotFoundError:
        print(f"{Fore.RED}Шлях {path} не існує.{Fore.WHITE}")
    except Exception as e:
        print(f"{Fore.RED}Помилка: {e}{Fore.WHITE}")

if __name__ == "__main__":
    # Перевіряємо формат вводу - 2 аргументи ОК - назва Скрипта і Шлях для Візуалізації
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Формат вводу: python 3-hw03.py c:/Python-Projects/goit-pycore-hw-04/{Fore.WHITE}")
    else:
        directory_path = sys.argv[1]
        viz_dir_struct(directory_path)