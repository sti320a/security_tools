#! python3


def generate_cryptogram(text: str, keynum: int) -> str:
    encrypted = ''
    for char in text:
        encrypted += chr(ord(char) + keynum)
    return encrypted


def try_decrypt(text: str) -> list:
    res = []
    for keynum in range(1, 27):
        res.append(generate_cryptogram(text, -keynum))
    return res


if __name__ == '__main__':
    print(generate_cryptogram('test', 1))
    try_decrypt('uftu')
