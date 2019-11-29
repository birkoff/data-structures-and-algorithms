class Node:

    def __init__(self, val, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def insert(self, new_val):
        if not self.val:
            self.val = new_val
            return

        if new_val < self.val:
            if not self.left:
                self.left = Node(new_val)
                return

            self.left.insert(new_val)
            return

        if new_val > self.val:
            if not self.right:
                self.right = Node(new_val)
                return

            self.right.insert(new_val)
            return

    def find(self, search_val):
        if search_val < self.val:
            if not self.left:
                return False

            return self.left.find(search_val)

        if search_val > self.val:
            if not self.right:
                return False

            return self.right.find(search_val)

        return True

    def traversal_level_order(self):
        # Breadth First
        queue = [self]
        while len(queue) > 0:
            print(queue[0].val)
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    def traversal_in_order(self, level=0):
        if self.val is None:
            return

        if self.left:
            self.left.traversal_in_order(level + 1)

        print("  -" * level + str(self.val))
        if self.right:
            self.right.traversal_in_order(level + 1)

    def traversal_pre_order(self, level=0):
        if self.val is None:
            return

        print("  -" * level + str(self.val))
        if self.left:
            self.left.traversal_pre_order(level + 1)

        if self.right:
            self.right.traversal_pre_order(level + 1)

    def traversal_post_order(self, level=0):
        if self.val is None:
            return

        if self.left:
            self.left.traversal_post_order(level + 1)

        if self.right:
            self.right.traversal_post_order(level + 1)

        print("  -" * level + str(self.val))


if __name__ == '__main__':
    # root = Node(1,  Node(2, None, Node(4)), Node(3, None, Node(5)))
    root = Node(1,  Node(3, None, Node(5)), Node(2, None, Node(4)))
    # root.insert(6)
    # root.insert(89)
    # root.insert(34)
    # root.insert(23)
    # root.insert(1)
    # root.insert(3)
    # root.insert(6)
    # root.insert(14)
    # root.insert(7)

    print("traversal_in_order:")
    root.traversal_in_order()
    print("traversal_level_order")
    root.traversal_level_order()
    print("traversal_post_order")
    root.traversal_post_order()
    print("traversal_pre_order")
    root.traversal_pre_order()