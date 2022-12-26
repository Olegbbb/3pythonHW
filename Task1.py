new_list = list(map(int, input("Введите элементы списка через пробел: ").split()))
print(f"Введенный список: \n {new_list}")
sum = 0
for i in range(1,len(new_list),2):
    sum += new_list[i]
print(f"Сумма нечетных элементов равна: {sum}")