#THIS IS CALCULATOR PROGRAM
#Intro to user
print("Hey ! \nThis is the calculator where you can do \nAddition, Substraction, Multiplication ,Division , Power ,Modulo.  ")

#Taking input from user

n= int(input("Enter number : "))
m=int(input("Enter number : "))
oppo=input("Enter  opperation [+, -, /, *, **, %] : ")

#Calculation done here

if(oppo=="+"):
       print("Addition of entered number is....\n ", n, "+", m, "=" , n+m )

elif(oppo=="-"):
       print("Substraction of entered number is....\n ", n, "-", m, "=" , n-m )

elif(oppo=="*"):
       print("Multiplicationn of entered number is....\n ", n, "*", m, "=" , n*m )

elif(oppo=="/"):
       print("Divisionon of entered number is....\n ", n, "/", m, "=" , n/m )
        
elif(oppo=="**"):
       print("Power of n = ",  n**m )

elif(oppo=="%"):
       print("Modulo of entered number is....\n ", n, "%", m, "=" , n%m )
       
   #end    
       
       

