class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return ""

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return ""

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

inputs = input('Enter Input : ').split(',')

trees = Stack()

for instruction in inputs:
    if instruction[0] == 'A':
        trees.push(int(instruction[2:]))

    elif instruction[0] == 'B':
        temp = Stack()
        highest = 0
        count = 0
        while not trees.isEmpty():
            height = original_height = trees.pop()
            temp.push(original_height)
            if height > highest:
                highest = height
                count += 1
            else:
                break
        print(count)
        while not temp.isEmpty():
            trees.push(temp.pop())

    elif instruction[0] == 'S':
        temp = Stack()
        while not trees.isEmpty():
            temp.push(trees.pop())
        while not temp.isEmpty():
            height = temp.pop()
            if height % 2 == 0:
                height -= 1
                if height < 1:
                    height = 1
            else:
                height += 2
            trees.push(height)