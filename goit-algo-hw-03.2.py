import random

def get_numbers_ticket(min, max, quantity):
    list = []
    if min >= 1 and max <= 1000 and min < quantity < max:
        list.append(min)
        for i in range(quantity):
            num = random.randint(min, max)
            list.append(num)
        list.append(max)
    return sorted(list)

print(get_numbers_ticket(1, 49, 6))
