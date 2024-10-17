def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            
            for line in file:
                
                name, salary = line.strip().split(',')
                
                
                total += int(salary)
                count += 1
            
            
            average = total / count if count > 0 else 0
            
            return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except ValueError:
        print("Некоректні дані у файлі.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


result = total_salary('test.txt')
print(result)