class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        for ele in self.items:
            s += str(ele) + ""
        return s

    def push(self, i):
        self.items.append(i)
        
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

def match(open, close):
    return (open == "(" and close == ")") or \
        (open == "[" and close == "]") 

def parenMatching(str):
    s = Stack()
    i = 0
    error = 0

    while i < len(str) and error == 0:
        c = str[i]
        if c in "([":
            s.push(c)
        else :
            if c in ")]":
                if s.size() > 0:
                    if not match(s.pop(), c):
                        error = 1
                else:
                    error = 2
        i += 1
    
    if s.size() > 0:
        error = 3
    return error, c, i, s

inp = input("Enter Input : ")
err, c, i, s = parenMatching(inp)
if err == 0:
    print("Parentheses : Matched ! ! !")
    
else:
    print("Parentheses : Unmatched ! ! !")