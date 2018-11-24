d = {}

def update_dictionary(d, key, value):

    if key in d:
        d[key].append(value)
    else:
        key1 = key * 2
        if key1 not in d:
            d[key1] = []

        d[key1].append(value)

print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}