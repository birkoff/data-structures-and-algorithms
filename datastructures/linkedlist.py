class LinkedList:
    def __init__(self, head=None):
        self.length = 0
        self.head = head

    def add(self, data):
        """
        Inserts at the begining on the List
        node.prev = None
        node.next = self.head
        """
        new_node = Node(data)
        new_node.prev = None

        self.length = self.length + 1

        if self.head:
            new_node.next = self.head
            new_node.next.prev = new_node

        self.head = new_node

    def insert(self, data, position):
        new_node = Node(data)
        match = False
        current = self.head
        i = 0
        while current and match is False:
            if i == position:
                match = True
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                self.length = self.length + 1
            else:
                current = current.next
            i += 1
        return current

    def insert_after(self, data, after):
        """
        Inserts at specific position on the List
        new_node.prev = after
        new_node.next = after.next
        new_node.prev.next = new_node
        new_node.next.prev = new_node
        """
        new_node = Node(data)
        match = False
        current = self.head
        while current and match is False:
            if current.data == after:
                match = True
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                self.length = self.length + 1
            else:
                current = current.next
        return current

    def append(self, data):
        """
        Inserts at the End of the List
        node.prev = self.head
        node.next = None
        """
        new_node = Node(data)
        new_node.next = None
        new_node.prev = None

        self.length = self.length + 1

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        new_node.prev = current
        current.next = new_node

    def remove(self, data):
        if not self.head:
            return

        current = self.head
        prev = None

        match = False
        while current:
            if current.data == data:
                match = True
                break

            prev = current
            current = current.next

        if not match:
            return

        self.length = self.length - 1
        prev.next = current.next
        current = None

    def traverse(self):
        current = self.head
        list = []
        while current:
            # next_data = current.next.data if current.next else None
            list.append("{}".format(current.data))
            current = current.next
        return list

    def has_cycle(self):
        head = self.head
        prev = None
        while head:
            if (prev and head.next and prev == head.next) or hasattr(head, 'visited'):
                return 1
            head.visited = True
            prev = head
            head = head.next
        return 0

    def __len__(self):
        return self.length


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    mylist = LinkedList()
    mylist.append("16")
    mylist.append("13")
    mylist.append("7")
    # mylist.add("four")
    # mylist.append("five")
    # mylist.append("six")
    # mylist.append("seven")
    # mylist.append("eight")
    # mylist.add("nine")
    # mylist.append("ten")
    # mylist.traverse()
    # mylist.remove("eight")
    # mylist.remove("five")
    # mylist.traverse()
    mylist.insert("nine", after="eight")
    # mylist.insert("four", after="three")

    for item in mylist.traverse():
        print(item, end=' ')

