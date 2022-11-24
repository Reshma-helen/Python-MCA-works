
n=int(input("Enter step number"))
def pattern(n):
    
    for i in range(1,n+1):
        print()
        for j in range(1,i+1):
            print(j*i,end=" ")



pattern(n)
