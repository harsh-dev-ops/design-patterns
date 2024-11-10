
from enum import Enum
from typing import List


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        LPAREN = 3
        RPAREN = 4

    def __init__(self, type, text: str) -> None:
        self.type = type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


def lex(input: str):
    input = input.replace(' ', '')
    result = []

    hash_map = {
        '+': Token.Type.PLUS,
        '-': Token.Type.MINUS,
        '(': Token.Type.LPAREN,
        ')': Token.Type.RPAREN
    }

    i = 0
    while i < len(input):
        if input[i] in hash_map:
            result.append(
                Token(hash_map[input[i]], input[i])
            )
        else:  # integer
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    result.append(
                        Token(
                            Token.Type.INTEGER,
                            ''.join(digits)
                        )
                    )
                    break
        i = i + 1

    return result


def eval(input):
    tokens = lex(input)

    print(' '.join(map(str, tokens)))


if __name__ == '__main__':
    exp = '(13 + 4) - (12+1)'

    eval(exp)
