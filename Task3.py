from random import randint, uniform
my_list = []
for i in range(10):
    k = randint(0, 3)
    my_list.append(round(uniform(0, 10), k))
print(my_list)
new_list = []
for i in my_list:
    if i != int(i):
        new_list.append(round(i - int(i),3))
print(f"Разница между {max(new_list)} и {min(new_list)} равна: {max(new_list) - min(new_list)}")
