def total_salary(path):
    try: # Читання файлу 
        with open(path, encoding='utf-8') as file:
            # Змінні загальної зарплатні та підрахунку розробників
            total_salary = 0
            count_developers = 0
            for line in file:
                # Видаляємо пробіли і ділимо за комою
                salary_file = line.strip().split(',')
                name = salary_file[0]
                salary = salary_file[1]
                salary = float(salary)
                # Рахуємо загальну зарплатню і к-сть розробників
                total_salary += salary
                count_developers += 1
            # Розрахунок середньої заробітної плати
            if count_developers > 0:
                average_salary = total_salary / count_developers
            else:
                average_salary = 0
            return total_salary, average_salary
    except FileNotFoundError:
        print(f"Файл відсутній або пошкоджений")
        return 0, 0

total, average = total_salary("salary_file.txt")
total = round(total)
average = round(average)

if total > 0 and average > 0:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")