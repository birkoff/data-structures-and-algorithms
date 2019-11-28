class MyQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add(self, item):
        self.items.append(item)

    def consume(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def next(self):
        if self.is_empty():
            return None

        return self.items[0]

# Actions:
# 1 x: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.


def calculate(data):

    my_queue = MyQueue()
    next_items = []

    for line in data:
        action = int(line.pop(0))
        value = int(line.pop()) if len(line) else None

        if action == 1 and value > 0:
            my_queue.add(value)
            continue

        if action == 2:
            my_queue.consume()

        if action == 3:
            next_items.append(my_queue.next())

    return next_items


if __name__ == '__main__':
    the_input = []
    # with open('input.txt', 'r') as raw_input:
    #     total = int(raw_input.readline().rstrip())
    #     for _ in range(total):
    #         the_input.append(list(map(int, raw_input.readline().rstrip().split())))

    total = int(input().rstrip())
    for _ in range(total):
        the_input.append(list(map(int, input().rstrip().split())))

    result = calculate(the_input)

    # with open('output.txt', 'w') as output:
    for r in result:
        print(str(r) + '\n')

