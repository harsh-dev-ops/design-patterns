def _qualified_name(obj: object):
    return obj.__module__ + '.' + obj.__qualname__


def _declared_class_name(obj):
    name = _qualified_name(obj)
    return name[:name.rfind('.')]


_methods = {}


def _visitor_implementation(self, arg):
    method = _methods[(_qualified_name(type(self)), type(arg))]
    return method(self, arg)


def visitor(arg_type):
    def decorator(fn):
        _methods[(_declared_class_name(fn), arg_type)] = fn
        return _visitor_implementation

    return decorator


class DoubleExpression:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(
        self,
        left: DoubleExpression,
        right: DoubleExpression
    ):
        self.left = left
        self.right = right


class ExpressionPrinter:
    def __init__(self) -> None:
        self.buffer = []

    @visitor(DoubleExpression)
    def visit(self, de: DoubleExpression):
        self.buffer.append(str(de.value))

    @visitor(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        self.buffer.append('(')
        self.visit(ae.left)
        self.buffer.append('+')
        self.visit(ae.right)
        self.buffer.append(')')

    def __str__(self):
        return ''.join(self.buffer)


class ExpressionEvaluator:
    def __init__(self) -> None:
        self.value = None

    @visitor(DoubleExpression)
    def visit(self, de: DoubleExpression):
        self.value = de.value

    @visitor(AdditionExpression)
    def visit(self, ae: AdditionExpression):
        self.visit(ae.left)
        temp = self.value
        self.visit(ae.right)
        self.value += temp

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    buffer = []
    printer = ExpressionPrinter()
    printer.visit(e)

    evaluator = ExpressionEvaluator()
    evaluator.visit(e)
    print(f"{printer} = {evaluator}")
