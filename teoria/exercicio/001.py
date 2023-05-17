# Primeira forma
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in a:
    if i % 2 == 0:
        print(i, 'é par.')
    else:
        continue

# Segunda forma
for i in range(12,31):
    if i % 2 == 0:
        print(i, 'é par.')
    else:
        continue
