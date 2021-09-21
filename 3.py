def myfunc(n):
    m = 1
    f = 1

    while True:
        f = f * m
        if(m == n):
            return f
        else:
            m += 1

n = int(input("ใส่จำนวนตัวเลข : "))
print (myfunc(n))