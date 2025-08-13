num = int(input("Enter your loop: "))
a = []
for i in range (num):
    num = int(input("Enter your data: "))
    if (10<= num <= 50):
        a.append(num)
print("ค่าที่อยู่ในช่วง 10-50: ",a)