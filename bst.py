class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)

        curr = self.root
        inserted = False

        while not inserted:
            if data < curr.data:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = Node(data)
                    inserted = True
            else:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = Node(data)
                    inserted = True

    def remove(self):
        pass

    def print_recursive_between(self, subtree, min, max):
        if subtree is None:
            return
        elif subtree.data < min:
            self.print_recursive_between(subtree.right, min, max)
        elif subtree.data > max:
            self.print_recursive_between(subtree.left, min, max)
        else:
            print(subtree.data)
            self.print_recursive_between(subtree.left, min, max)
            self.print_recursive_between(subtree.right, min, max)

    # BST's (wrapper) print_between function
    def print_between(self, min, max):
        self.print_recursive_between(self.root, min, max)


bs = BST()
bs.insert(7)
bs.insert(8)
bs.insert(2)
bs.print_between(0, 10)
