
 
'''num = int(input('Enter in a value: '))
total = 0
for i in range(0, num):
    total += int(str(num) + i * str(num))
print(total)'''


n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)
