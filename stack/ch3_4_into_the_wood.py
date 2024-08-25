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

stack = Stack()
inp = input('Enter Input : ').split(',')

for i in inp:
    if "A" in i:
        char, num = i.split(" ")
        stack.push(int(num))
    elif "B" in i:
        tempStack = Stack()
        if not stack.isEmpty():
            highest = stack.pop()
            tempStack.push(highest)
        while not stack.isEmpty():
            item = stack.pop()
            if item > highest:
                highest = item
                tempStack.push(item) 
        print(tempStack.size())
        while not tempStack.isEmpty():
            stack.push(tempStack.pop())