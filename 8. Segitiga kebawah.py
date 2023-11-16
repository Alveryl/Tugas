tinggi = 5

for i in range(tinggi, 0, -1):
    print(' ' * (tinggi - i) + '*' * i + '*' * (i - 1))