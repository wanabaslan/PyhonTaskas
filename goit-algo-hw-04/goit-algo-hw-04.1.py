def average_salary(path):
    total = 0
    count = 0
    with open(path, 'r') as file:
        for line in file:
            _, salary = line.strip().split(',')
            total += int(salary)
            count += 1
    average = total / count if count else 0
    return total, average 

file_path = 'salaries.txt'
total, average = average_salary(file_path)  

print(f"Загальна сума заробітної плати: {total}, середня заробітна плата: {average}")
