list_1=[-100,-23,98,63,0,-32,10]
list_2=[]
print("The given list is : ",list_1)

print("Positive numbers from given list of integers using list comprehension:")

for i in list_1:
    if i>=0:
        list_2.append(i)
print(list_2)


lst_1=[-100,-23,98,63,0,-32,10]
print("The given list is : ",lst_1)
print("Positive numbers from given list of integers using list comprehension:")
lst_2=[i for i in lst_1 if i>=0 ]
print(lst_2)

