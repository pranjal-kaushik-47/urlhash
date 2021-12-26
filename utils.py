from os import getenv

def encode(num, characters=getenv('characters')):
    if num == 0:
        return characters[0]
    arr = []
    base = len(characters)
    while num:
        num, rem = divmod(num, base)
        arr.append(characters[rem])
    arr.reverse()
    return ''.join(arr)

def decode(encoded, characters=getenv('characters')):
    base = len(characters)
    num = 0

    idx = 1
    for char in encoded:
        power = (len(encoded) - (idx))
        num += characters.index(char) * (base ** power)
        idx += 1
    return num