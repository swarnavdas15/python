#day8
#this is the program for calculating average using function

#defining Average funtion
def average(*num):
    sum=0
    for val in num :
         for i in val:
            sum+=i
    print("Average of your marks is ...\n", sum/len(val))

#Greeting user
print("Welcome to this Program! \nThis program is to calculate average marks ")

#taking input 
n=int(input("Enter number of marks to be enter : "))

marks=[]
for i in range(n):
     m=int(input("Enter marks : "))
     marks.append(m)


#Calling Function
average(marks)