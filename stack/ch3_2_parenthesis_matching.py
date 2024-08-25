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
        (open == "{" and close == "}") or \
        (open == "[" and close == "]")    

def parenMatching(str):
    s = Stack()
    i = 0
    error = 0

    while i < len(str) and error == 0:
        c = str[i]
        if c in "{[(":
            s.push(c)
        else :
            if c in "}])":
                if s.size() > 0:
                    if not match(s.pop(), c):
                        # open close not match
                        error = 1
                        break
                else:
                    # no open paren
                    error = 2
                    break
        i += 1
    
    if s.size() > 0 and error != 1:
        error = 3
    return error, c, i, s

inp = input("Enter expresion : ")
err, c, i, s = parenMatching(inp)
if err == 1:
    print(inp, "Unmatch open-close")
elif err == 2:
    print(inp, "close paren excess")
elif err == 3:
    print(inp, "open paren excess  ", s.size(), ": ", end="")
    for ele in s.items:
        print(ele, sep="", end="")
    print()
else:
    print(inp, "MATCH")