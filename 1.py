n = int(input("ใส่จำนวนของตัวเลข : "))

lst = list(map(int,input("ใส่ตัวเลข : ").strip().split()))[:n]

for i in range(len(lst)):
    for j in range(i + 1,len(lst)):

        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)