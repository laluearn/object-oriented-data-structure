print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = input("Enter Input : ").split()
# time
t = int(d)/ (int(Vt) - int(Vr))
# distance
s = t*(int(Vf))
print("{:.2f}".format(s))