class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.value}"


def inorder_traversal(node):
    def traverse(current):
        if current.left:
            for node in traverse(current.left):
                yield node

        yield current

        if current.right:
            for node in traverse(current.right):
                yield node

    for node in traverse(node):
        yield node


def preorder_traversal(node):
    def traverse(current):
        yield current

        if current.left:
            for node in traverse(current.left):
                yield node

        if current.right:
            for node in traverse(current.right):
                yield node

    for node in traverse(node):
        yield node


def post_order_traversal(node):
    def traverse(current):

        if current.left:
            for node in traverse(current.left):
                yield node

        if current.right:
            for node in traverse(current.right):
                yield node

        yield current

    for node in traverse(node):
        yield node


if __name__ == '__main__':

    #   1
    #  /  \
    # 2    3

    # inorder: 213
    # preorder: 123
    # postorder: 231

    root = Node(1, Node(2), Node(3))

    print("In order traversal")
    for node in inorder_traversal(root):
        print(node)

    print("\nPre order traversal")
    for node in preorder_traversal(root):
        print(node)

    print("\nPost order traversal")
    for node in post_order_traversal(root):
        print(node)
