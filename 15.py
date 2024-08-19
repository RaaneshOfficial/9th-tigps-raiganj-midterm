list1 = [5, 10, 15, 20]
list2 = [1, 2, 3, 4]
combined_list = [str(x) + str(y) for x in list1 for y in list2]

print("Combined List:", combined_list)