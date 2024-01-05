class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    append
    prepend

    pop_front_
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        self.size += 1

        # empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # non-empty list
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        self.size += 1

        # empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # non-empty list
        new_node.next = self.head
        self.head = new_node

    def pop_front(self):
        # empty
        if self.head is None:
            return None

        data = self.head.data

        # 1 node
        if self.head is self.tail:
            self.head = self.tail = None
            return data

        # 2+ nodes
        self.head = self.head.next
        return data

    def pop_back(self):
        # empty list
        if self.head is None:
            return None

        # 1 node
        if self.head is self.tail:
            data = self.head.data
            self.head = self.tail = None
            return data

        prev = self.head
        curr = self.head.next

        # advance prev and curr until you have last 2 nodes
        while curr.next is not None:
            prev = curr
            curr = curr.next

        # make prev the tail, and its next None
        self.tail = prev
        prev.next = None

    def search(self, pred):
        curr = self.head

        while curr:
            if pred(curr.data):
                return curr.data
            curr = curr.next

        return None

    def __str__(self):
        curr = self.head
        string = ''

        while curr is not None:
            string += str(curr.data) + ' -> '
            curr = curr.next

        string += 'None'
        return string


ll = LinkedList()
# ll.append(7)
# ll.append(8)
# ll.prepend(9)
ll.prepend([1, 2])

print(ll)

print('result: ', ll.search(lambda n: n[1] == 2))
