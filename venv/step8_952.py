a = int(input())
b = []
i = 1
while i <= a:
    j = 0
    while j < i:
        b.append(i)
        j += 1
    i += 1

for i in b[:a]:
    print(i, end=' ')
