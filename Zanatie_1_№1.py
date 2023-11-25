a = [10, 2, 4, 5, 9, 15, 236, 237, 12, 3, 4, 14, 27]

for n in a:
    if n % 2 == 0:
        print(n, end=' ')
    elif n == 237:
        break