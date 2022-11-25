a=input('enter the first string')
b=input('enter the second string')

a_temp=b[0:1]+a[1:]
b_temp=a[0:1]+b[1:]
a,b=a_temp,b_temp
print("After swapping")
print(a,b)
