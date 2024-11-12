def get_matrix(n, m, value):  
    matrix = []  # Создаем пустой список для матрицы  
    for i in range(n):  # Внешний цикл для количества строк  
        row = []  # Создаем пустой список для строки  
        for j in range(m):  # Внутренний цикл для количества столбцов  
            row.append(value)  # Добавляем значение value в строку  
        matrix.append(row)  # Добавляем заполненную строку в матрицу  
    return matrix  # Возвращаем матрицу  

# Примеры вызова функции  
result1 = get_matrix(2, 2, 10)  
result2 = get_matrix(3, 5, 42)  
result3 = get_matrix(4, 2, 13)  

# Выводим результаты на консоль  
print(result1)  
print(result2)  
print(result3)