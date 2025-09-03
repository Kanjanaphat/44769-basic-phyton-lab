num = int(input("Enter your loop: "))
count = 0
for i in range (num):
    num = int(input("Enter your data: "))
    if (num > 50):
        count += 1
print("จำนวนที่มากกว่า 50: ",count)