def get_cats_info(path):
    cats = []
    
    try:
        
        with open(path, 'r', encoding='utf-8') as file:
            
            for line in file:
                
                line = line.strip()
                
                
                if line:
                    
                    cat_data = line.split(',')
                    
                    
                    if len(cat_data) == 3:
                        
                        cat = {
                            "id": cat_data[0].strip(),  
                            "name": cat_data[1].strip(),  
                            "age": int(cat_data[2].strip())  
                        }
                        
                        cats.append(cat)
                    else:
                        print(f"Некоректний рядок у файлі: {line}")
    
    except FileNotFoundError:
        print(f"Файл не знайдено за шляхом: {path}")
    except ValueError as e:
        print(f"Помилка при обробці даних: {e}")
    except Exception as e:
        print(f"Невідома помилка: {e}")
    
    return cats

result = get_cats_info('2.txt')
print(result)