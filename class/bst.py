import queue


class BST:

    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    # Iterative insert

    def insert_iterative(self, data):
        # empty bst
        if self.root is None:
            self.root = self.Node(data)
            return

        # non-empty bst
        curr = self.root
        inserted = False

        while not inserted:
            # new data < than node's value
            if data < curr.data:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = self.Node(data)
                    inserted = True

            # new data > than node's value
            else:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = self.Node(data)
                    inserted = True

    # Iterative search

    def search_iterative(self, data):
        curr = self.root

        while curr is not None:
            if data < curr:
                curr = curr.left
            elif data > curr:
                curr = curr.right
            else:  # data == curr.data case
                return curr

        return None  # not found

    # Iterative BFT print

    def bft_print_iterative(self):
        nodes = queue.Queue()

        # 1. prime queue with root
        if self.root is not None:
            nodes.put(self.root)

        # 2.
        while not nodes.empty():
            # dequeue
            curr = nodes.get()

            # enqueue non-null children
            if curr.left:
                nodes.put(curr.left)
            if curr.right:
                nodes.put(curr.right)

            # print dequeued node
            print(curr.data, end=" ")

    ########################################################################

    # Recursive search

    def r_search(self, data, subtree):
        if subtree is None:
            return None

        if data < subtree.data:
            return self.r_search(data, subtree.left)
        if data < subtree.data:
            return self.r_search(data, subtree.right)

        return subtree

    def search_recursive(self, data):
        return self.r_search(data, self.root)

    # Recursive insert

    def r_insert(self, data, subtree):
        if subtree is None:
            return self.Node(data)
        elif data < subtree.data:
            subtree.left = self.r_insert(data, subtree.left)
            return subtree
        elif data > subtree.data:
            subtree.right = self.r_insert(data, subtree.right)
            return subtree

    def insert_recursive(self, data):
        self.root = self.r_insert(data, self.root)

    # Recursive inorder print

    def r_print_inorder(self, subtree):
        if subtree is not None:
            self.r_print_inorder(subtree.left)
            print(subtree.data, end=" ")
            self.r_print_inorder(subtree.right)

    def print_inorder(self):
        self.r_print_inorder(self.root)

    # Recursive preorder print

    def r_print_preorder(self, subtree):
        if (subtree != None):
            print(subtree.data, end=" ")
            self.r_print_preorder(subtree.left)
            self.r_print_preorder(subtree.right)

    def print_preorder(self):
        self.r_print_preorder(self.root)

    def __str__(self):
        lines, *_ = self._display_aux(self.root)
        return '\n'.join(lines)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def depth_first_traversal(self):
        if self.root is None:
            return

        s = []  # stack
        s.append(self.root)

        while len(s) > 0:
            curr = s.pop()  # pop the top item from the stack
            print(curr.data)

            if curr.right is not None:
                s.append(curr.right)  # add right child to the stack
            if curr.left is not None:
                s.append(curr.left)  # add left child to the stack

    def r_depth_first_traversal(self, subtree):
        if subtree is None:
            return

        print(subtree.data)
        self.r_depth_first_traversal(subtree.left)
        self.r_depth_first_traversal(subtree.right)

    def sum_of_nodes(self):
        def r_sum(subtree):
            if subtree is None:
                return 0
            return subtree.data + r_sum(subtree.left) + r_sum(subtree.right)

        return r_sum(self.root)

    def depth_of_node(self, data):
        if self.root is None:
            return -1

        depth = 0
        curr = self.root

        while curr:
            if curr.data == data:
                return depth

            if curr.data > data:
                curr = curr.left
            elif curr.data < data:
                curr = curr.right

            depth += 1

        return -1

    def depth_r(self, data):
        def r(subtree, data):
            if subtree is None:
                return -1

            if subtree.data > data:
                return 1 + r(subtree.left, data)
            elif subtree.data < data:
                return 1 + r(subtree.right, data)
            return 0

        return r(self.root, data)

    def sum_of_leafs(self):
        def r_sum(subtree):
            if subtree is None:
                return 0
            if subtree.right is None and subtree.left is None:
                return subtree.data + r_sum(subtree.left) + r_sum(subtree.right)

            return r_sum(subtree.left) + r_sum(subtree.right)

        return r_sum(self.root)


b = BST()
b.insert_iterative(8)
b.insert_iterative(2)
b.insert_iterative(1)
b.insert_iterative(3)
b.insert_iterative(5)
b.insert_iterative(4)
b.insert_iterative(12)
b.insert_iterative(7)
b.insert_iterative(18)

print(b)
print(b.depth_r(73))
