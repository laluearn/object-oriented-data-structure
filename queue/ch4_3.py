code, hint = input("Enter code,hint : ").split(",")
diff = ord(hint) - ord(code[0])

ans = []

for i in code:
    ans.append(chr(ord(i) + diff))
    print(ans)