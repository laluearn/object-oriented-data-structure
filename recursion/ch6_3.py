def parenthesis(num, open, close, s, ans):
    if open == num and close == num:
        ans.append(s)
        return

    if open < num:
        parenthesis(num, open + 1, close, s + "(", ans)

    if close < open:
        parenthesis(num, open, close + 1, s + ")", ans)

num = int(input("Enter number of pair parenthesis(es): "))
print("All possible parenthesis(es)")
ans = []
parenthesis(num, 0, 0, "", ans)
if ans:
    print(",".join(ans))