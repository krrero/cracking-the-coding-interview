# O(n^2) >:(

check = "abcdefghijklmnopqrstuvwxyz Aa"

is_unique = True

for i, character in enumerate(check):
    for j, char in enumerate(check):
        if i != j and char == character:
            is_unique = False
            break

if is_unique:
    print('The string is unique :D')
else:
    print('The string is not unique :(')