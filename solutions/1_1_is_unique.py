# Time complexity O(n) >:D


def is_unique_chars(word : str) -> bool:
    if len(word) > 128: 
        return False

    char_set = [0] * 128

    for character in word:
        char_int = ord(character)

        if char_set[char_int] == 1:
            return False
        
        char_set[char_int] = 1
    
    return True


if __name__ == '__main__':
    is_unique = is_unique_chars('abcdefghf')

    if is_unique:
        print('The string is unique :D')
    else:
        print('The string is not unique :(')