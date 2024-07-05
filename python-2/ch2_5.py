class funString():

    def __init__(self,string = ""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self) :
        return len(self.string)

    def changeSize(self):
        newlist = []
        for ch in self.string:
            if 'A' <= ch <= 'Z' : newchar = chr(ord(ch) + 32)
            elif 'a' <= ch <= 'z' : newchar = chr(ord(ch) - 32)
            else: newchar = ch
            newlist.append(newchar)
        return "".join(newlist)

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        seen = []
        for ch in self.string:
            if ch not in seen: seen.append(ch)
        return "".join(seen)


str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" : print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())