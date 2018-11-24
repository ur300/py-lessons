#info = 'a3b4c2e10b11'
#aaabbbbcceeeeeeeeeeb
res = ''
info = ''
num = ''
symbol = ''
i = 0
with open('dataset_3363_2.txt') as inp:
    info = inp.readline()

while(i < len(info)):
    if info[i].isdigit():
        num += info[i]
    else:
        if num != '' and symbol != '':
            res += symbol * int(num)

        symbol = info[i]
        num = ''
    i += 1

if num != '' and symbol != '':
    res += symbol * int(num)

with open('output_3363_2.txt', 'w') as out:
    out.write(res)