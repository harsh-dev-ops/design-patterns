from abc import ABC


class Expression(ABC):
    pass


class DoubleExpression(Expression):
    def __init__(self, value: int):
        self.value = value


class AdditionExpression(Expression):
    def __init__(
        self,
        left: DoubleExpression,
        right: DoubleExpression
    ) -> None:

        self.left = left
        self.right = right


class ExpressionPrinter:
    @staticmethod
    def print(e: Expression, buffer: list):
        if isinstance(e, DoubleExpression):
            buffer.append(str(e.value))
        elif isinstance(e, AdditionExpression):
            buffer.append('(')
            ExpressionPrinter.print(e.left, buffer)
            buffer.append('+')
            ExpressionPrinter.print(e.right, buffer)
            buffer.append(')')

    Expression.print = lambda self, b: \
        ExpressionPrinter.print(self, b)


if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []

    e.print(buffer)

    print(''.join(buffer))
