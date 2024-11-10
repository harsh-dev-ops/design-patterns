
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


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value


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


class BinaryOperation:
    class Type(Enum):
        ADDITION = 0
        SUBTRACTION = 1

    def __init__(self,):
        self.type = None
        self.left: Integer = None
        self.right: Integer = None

    @property
    def value(self):
        if self.type == BinaryOperation.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == BinaryOperation.Type.SUBTRACTION:
            return self.left.value - self.right.value


def parse(tokens: List[Token]):
    result = BinaryOperation()
    have_lhs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token.type == Token.Type.PLUS:
            result.type = BinaryOperation.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryOperation.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j = j + 1

            subexpression = tokens[i+1: j]
            element = parse(subexpression)

            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        elif token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        i = i + 1
    return result


def eval(input):
    tokens = lex(input)

    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)

    print(f"{input} = {parsed.value}")


if __name__ == '__main__':
    exp = '(13 + 4) - (12+1)'

    eval(exp)
