#'a aa abC aa ac abc bcd a AA'

wordsList = input().lower().split()
resDict = {}

for w in wordsList:
    if w in resDict:
        resDict[w] += 1
    else:
        resDict[w] = 1

for key in resDict:
    print(key, resDict[key])

count_words('a aa abC aa ac abc bcd a')