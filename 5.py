class calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b

my_cal = calculator()

while True:
    print("1: บวก")
    print("2: ลบ")
    print("3: คูณ")
    print("4: หาร")
    print("5: ออกจากโปรแกรม")

    ch = int(input("เลือกเครื่องมือ: "))

    if(ch == 5):
        break

    a = int(input("ใส่เลขตัวที่1 : "))
    b = int(input("ใส่เลขตัวที่2 : "))

    if(ch == 1):
        print(my_cal.add(a, b))
    elif(ch == 2):
        print(my_cal.subtract(a, b))
    elif(ch == 3):
        print(my_cal.multiply(a, b))
    elif(ch == 4):
        if(b == 0):
            print("ไม่สามารถหารด้วย 0 ได้")
        else:
            print(my_cal.divide(a, b))
    else:
        print("ERROR!!!!")