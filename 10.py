marks = []
a = float(input("Marks 1:"))
marks.append(a)
b = float(input("Marks 2:"))
marks.append(b)
c = float(input("Marks 3:"))
marks.append(c)

average = sum(marks) / len(marks)
print("Average marks:",average)