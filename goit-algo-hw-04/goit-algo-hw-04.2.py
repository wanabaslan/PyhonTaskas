def get_cats_info(path):
    cats = []  
    with open(path, 'r') as file:
        for line in file:
            id, name, age = line.strip().split(',')  
            cats.append({"id": id, "name": name, "age": age}) 
    return cats

cats_info = get_cats_info('cats.txt')
print(cats_info)
