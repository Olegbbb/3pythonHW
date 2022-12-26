num = int(input("Введите число: "))
binary = []
while num > 0:
    binary.append(str(num % 2))
    num = num // 2
binary.reverse()
binary = "".join(binary)
print(f"Двоичная система: {binary}")
