n = int(input("ใส่จำนวนตัวเลข : "))
g3 = []
g5 = []
g7 = []

for i in range(1, n+1):
    if (i%3==0):
        g3.append(i)
    if i not in g3:
        if (i%5==0):
            g5.append(i)
    if i not in g3 and i not in g5:
        if (i%7==0):
            g7.append(i)


print("group#3 : {}".format(g3))
print("group#5 : {}".format(g5))
print("group#7 : {}".format(g7))