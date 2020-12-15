#ist1 = ['physics', 'chemistry', 1997, 2000]
#list2 = [1, 2, 3, 4, 5 ]
#list3 = ["a", "b", "c", "d"]


#Accessing Values in Lists


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print(f"list1[0]: ", list1[0])
print(f"list2[1:5]: ", list2[1:5])


print("\n")

#Updating Lists
list = ['physics', 'chemistry', 1997, 2000]
print("Value available at index 2 : ")
print(list[2])
list[2] = 2001
print("New value available at index 2 : ")
print(list[2])


print("\n")
#Delete List Elements

list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)