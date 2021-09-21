n = list(map(int,input("ใส่ตัวเลข : ").strip().split()))[:2]

while(n[1]):
    n[0],n[1] = n[1],n[0]%n[1]

print(n[0])