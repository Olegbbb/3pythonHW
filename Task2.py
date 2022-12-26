from random import randint
elem_amount = randint(3, 7)
new_list = [randint(1, 9) for i in range(0, elem_amount)]
print(f"Наш список: {new_list}")
result =[]
for i in range(0, len(new_list)//2):
    result.append(new_list[i] * new_list[len(new_list) - 1 - i])
if elem_amount % 2 > 0:
    result.append(new_list[len(new_list)//2]**2)
print(f"Результат: {result}")