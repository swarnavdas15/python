#functions
#factorial
def fact (n):
    if (n==0 | n==1):
        return 1
    else:
        return n*fact(n-1)

 #fabonacci series   
def fabo(m):
    f0, f1 = 0, 1
    print(f0, f1, sep="\n")
    for val in range(n):
        sum = f0+f1
        print(sum)
        f0,f1 = f1,sum

#greeting
for i in range(50):
    print("-", end="")
    
name=input("\nEnter your name : ")
print(f"Hi! {name}...")
print("This is the program to calculate factorial ")
    
n=int(input("Enter number to find to find factorial: "))
print("Factorial is ...\n", fact(n))

m=int(input("Enter number to find to find fabonacci series: "))
fabo(m)
print("End")