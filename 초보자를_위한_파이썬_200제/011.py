scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x, end=' ')
print()

for x in range(10):
    print(x, end=', ')
print()

for x in range(1, 10, 2):
    print(x, end=', ')
print()

for x in range(10, 1, -2):
    print(x, end=', ')
print()

str = 'abcdef'
for c in str:
    print(c, end=' ')
print()

for x in scope:
    print(x, end=' ')
    if x < 3:
        continue
    else:
        break