def length(txt):
    if txt == "":
        return 0
    leng = 1 + length(txt[:-1])
    if leng%2 == 0:
        print(txt[-1]+'~',end="")
    else:
        print(txt[-1]+'*',end="")
    return leng

print("\n",length(input("Enter Input : ")),sep="")