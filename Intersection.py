list1 = []

list2 = []

size1 = int(input("Enter the size of the first list : "))

size2 = int(input("Enter the size of the second list : "))

print("For the first list : ")

for i in range(0, size1):

    e = int(input("Enter element for position {} : ".format(i)))

    list1.append(e)

print("For the second list : ")

for i in range(0, size2):

    e = int(input("Enter element for position {} : ".format(i)))

    list2.append(e)

list_intersection = list(set(list1) & set(list2))

print("Intersection of {} and {} is : {}".format(

    list1, list2, list_intersection))
