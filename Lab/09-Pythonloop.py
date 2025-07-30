multiply = int(input("Multiplication table : "))
for number in range(1 , 12):
    print(multiply * (number + 1))


#for number in range(12): 12 ครั้ง
#for number in range(1 , 12): เริ่ม 1 - 12
#for number in range(1 , 12 , 3 ) เพิ่มทีละ 3
fruits = ["apple" , "banana" , "cherry"]
for x in fruits:
    print (x)
    if x == "banana":
        break