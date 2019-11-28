class LinkedList:
    def __init__(self):
        self.length = 0
        self.current = None

    def append(self, val, after=None):
        node = Node(val)
        self.length = self.length + 1

        if after is None:
            if self.current:
                node.next = self.current

            self.current = node
        else:
            current = self.current
            match = False
            while current:
                if current.val == after:
                    match = True
                    break

                current = current.next

            if not match:
                return

            node.next = current.next
            current.next = node

            self.length = self.length + 1

    def add(self, val):
        node = Node(val)
        self.length = self.length + 1

        if not self.current:
            self.current = node
            return

        current = self.current
        while current.next:
            current = current.next

        current.next = node

    def remove(self, val):
        if not self.current:
            return

        current = self.current
        prev = None

        match = False
        while current:
            if current.val == val:
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
        current = self.current
        list = []
        while current:
            next_val = current.next.val if current.next else None
            list.append("{} -> {}".format(current.val, next_val))
            current = current.next
        print(list)

    def has_cycle(self):
        head = self.current
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
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


mylist = LinkedList()
mylist.add("one")
mylist.add("two")
mylist.add("three")
mylist.add("four")
mylist.add("five")
mylist.add("six")
mylist.add("seven")
mylist.add("eight")
mylist.add("nine")
mylist.add("ten")
mylist.traverse()
mylist.remove("five")
mylist.remove("eight")
mylist.traverse()
mylist.append("five", after="four")
mylist.append("seven", after="seven")
mylist.traverse()
