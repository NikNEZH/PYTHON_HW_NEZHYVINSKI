i = 0
j = 0
for i in range(1, 10):
    if i % 10 == 0:
        print(" ")
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}\t', end=" ")
        if j % 10 == 0:
            print(" ")