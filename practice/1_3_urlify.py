
def urlify(string: str) -> str:
    return string.rstrip().lstrip().replace(" ", "%20")


if __name__ == '__main__':
    print( "-" + urlify("Mr John Smith      ") + "-")