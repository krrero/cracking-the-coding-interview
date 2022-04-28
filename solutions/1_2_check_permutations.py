# Solution 1: Sort the strings

def sort_string(a):
    return "".join(sorted(a))


a = "ABCDA"
b = "BDCXA"

a_sorted = sort_string(a)
b_sorted = sort_string(b)

if len(a_sorted) != len(b_sorted):
    print("The strings are not permutations of each other")

elif a_sorted == b_sorted:
    print("The strings are permutations of each other")



# Solution 2: Check if the two strings have identical character counts

def permutations(a, b):
    is_permutation = True 

    if len(a) != len(b):
        is_permutation = False

    letters = { char: a.count(char) for char in a }

    for char in b:
        if char not in letters:
            is_permutation = False
            break

        letters[char] -= 1 

        if letters[char] < 0:
            is_permutation = False

    return is_permutation



if permutations(a, b):
    print("The strings are permutations of each other")