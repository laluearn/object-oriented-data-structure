class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

def prec(c):
    if c == "^":
        return 3
    elif c == "/" or c =="*":
        return 2
    elif c == "+" or c == "-":
        return 1
    else:
        return 0

def isOperand(c):
    return ('a'<= c <= 'z' or 'A' <= c <= 'Z' or "0" <= c <= "9")

def infixToPostfix(c):
    stack = Stack()
    postFix = []

    for i in range(len(c)):
        if isOperand(c[i]):
            postFix.append(c[i])
        elif c[i] == '(':
            stack.push(c[i])
        elif c[i] == ')':
            while stack.peek() != '(':
                postFix.append(stack.peek())
                stack.pop()
            stack.pop() 
        else:
            while (not stack.isEmpty()) and (prec(c[i]) <= prec(stack.peek())):
                postFix.append(stack.pop())
            stack.push(c[i])

    while not stack.isEmpty():
        postFix.append(stack.peek())
        stack.pop()
    return "".join(postFix)

ch = input("Enter Infix : ")
ans = infixToPostfix(ch)
print("Postfix :",  ans)