list1=[1,2,3,4,5]
list2=[2,3,13,12,61,14]


if len(list1)==len(list2):
    print("Length of the two lists are equal \n")
else:

    print("Length of lists are not equal \n")


print("Sum of elements in list1 is:",sum(list1))
print("Sum of elements in list2 is:",sum(list2))

if sum(list1)==sum(list2):
    print("Sum of elements of two lists are equal")
else:
    print("Sum of elements of two lists are not equal \n\n")
   

print("The repeating elements are:")

for i in list1:
    if i in list2:
            print(i)
            

