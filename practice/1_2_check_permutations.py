# O(n!) >:((((

def toString(List):
    return ''.join(List)


def permute(a, string_b, l, r):
    if l==r:
        if string_b == toString(a):
            print(string_b + ' is a permutation of ' + toString(a) )
    else:
        for i in range(l,r):
            a[l], a[i] = a[i], a[l]
            permute(a, string_b, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack


string_a = "ABCD"
string_b = "DCBA"

n = len(string_a)
a = list(string_a)


permute(a, string_b, 0, n)