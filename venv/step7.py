list = input().split()
count = 1
dict = {}

for i in list[1:]:
    res = f(int(i))
    if not int(i) in dict:
        dict[int(i)] = res

for k in dict:
    print(dict[k])