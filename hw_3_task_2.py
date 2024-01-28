import random
def get_numbers_ticket(min, max, quantity):
    list_num = []
    while len(list_num)<quantity:
        a = random.randint(min, max)
        if a not in(list_num):
            list_num.append(a)
    print(f"Ваші лоторейні номери: {list_num}")

get_numbers_ticket(1, 35, 5)
