list1 = []
x = int(input("How many numbers do you want in the list:"))
for i in range(1,x+1):
    a = float(input("Enter number:"))
    list1.append(a)

total = sum(list1)
print("Sum of list:",total)