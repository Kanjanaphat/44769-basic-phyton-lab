num = int(input("Enter your loop: "))
numtotal = []
for i in range(num):
    num = int(input("Enter your data: "))
    numtotal.append(num)
total = max(numtotal)
total2 = min(numtotal)
print(total)
print(total2)