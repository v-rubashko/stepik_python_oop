number = int(input())

for i in range(number):
    temp = []
    for j in range(number):
        if i <= j and i + j < number:
            temp.append(i + 1)
        elif i <= j and i + j >=number:
            temp.append(number - j)
        elif i > j and i + j < number:
            temp.append(j + 1)
        else:
            temp.append(number - i)
    print(*temp, sep=' ')