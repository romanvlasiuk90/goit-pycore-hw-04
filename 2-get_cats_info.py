def get_cats_info(path):
    # Створюємо словник для усіх котів
    cats_info = []
    try: # Читаємо файл
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок по комі та передаємо значення ідентифікатор, ім'я та вік кота у кортеж
                cat = line.strip().split(',')
                # Доповнюємо словник інформацією про кота з кортежу
                cat_info = {"id": cat[0], "name": cat[1], "age": cat[2]}
                cats_info.append(cat_info)
        return cats_info
    except FileNotFoundError:
        return (f"Файл не знайдено")

all_cats_info = get_cats_info("cats_file.txt")
print(all_cats_info)