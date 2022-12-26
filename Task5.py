num = abs(int(input("Введите число ")))
while num == 0:
    num = abs(int(input("Введите число ")))
fibonachi = [1,1]
negafibonachi = [-1,1,0]
if num == 1:
    print('[1, 0, 1]')
else:
    for i in range(0,num -2):
        fibonachi.append(fibonachi[i] + fibonachi[i + 1])
        negafibonachi.insert(0,negafibonachi[1] - negafibonachi[0])
    negafibonachi.extend(fibonachi)
    print(negafibonachi)

