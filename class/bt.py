"""
BT - bfs, dfs
BST - Insert, Search
"""

"""
BFS
Traversal by height. Left to right, then level down.
"""




import queue
class BT:
    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def breadth_first_traversal(self):
        if self.root is None:
            return

        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            curr = q.get()  # get first item in the queue
            print(curr.data)  # print the data

            if curr.left is not None:
                q.put(curr.left)  # add left child to the queue
            if curr.right is not None:
                q.put(curr.right)  # add right child to the queue

    def recursive_bft(self):
        if self.root is None:
            return

        q = queue.Queue()
        q.put(self.root)

        self.recursive_bft_helper(q)

    def recursive_bft_helper(self, q):
        if q.empty():
            return

        curr = q.get()
        print(curr.data)

        if curr.left is not None:
            q.put(curr.left)
        if curr.right is not None:
            q.put(curr.right)

        self.recursive_bft_helper(q)

    def depth_first_traversal(self):
        if self.root is None:
            return

        s = []
        s.append(self.root)

        while len(s) > 0:
            curr = s.pop()
            print(curr.data)

            if curr.right is not None:
                s.append(curr.right)
            if curr.left is not None:
                s.append(curr.left)


bt = BT()


bt.depth_first_traversal()
