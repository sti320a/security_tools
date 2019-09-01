#! python3


def generate_cryptogram(text: str, keynum: int) -> str:
    encrypted = ''
    for char in text:
        encrypted += chr(ord(char) + keynum)
    return encrypted


if __name__ == '__main__':
    print(generate_cryptogram('test', 1))
