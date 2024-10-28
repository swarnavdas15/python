#Serial number generator 
import time as t

# Greeting  user with time stamp
def timestamp ():
     time = t.strftime('%H:%M %p')
     H=int(t.strftime('%H'))

     if (H>=6) & (H<12):
        print("GOOD MORNING SIR! \nItS->", end=" ")
        print(time , "\nHAVE A GOOD DAY AHEAD !")
     elif(H>=12) & (H<16):
        print("GOOD AFTERNOON SIR! \nItS-> " , end=" ")
        print(time , '\nHAVE A BREAK SIR !')
     elif(H>=16) & (H<21):
        print("GOOD EVENING SIR! \nItS-> " , end=" ")
        print(time , '\nENJOY YOUR TIME SIR !')
     else:
         print("GOOD NIGHT SIR! \nItS-> ",  end=" ")
         print(time , '\nHAVE A GOOD SLEEP !')

#Designing line
def line():
     for val in range (50):
         print("-", end ="")

#Defining serial number generator 
def serialno(n, sr):
      for val in range(n):
          temp=sr+str(val)
          dict.update({val:temp})
          print(dict.get(val))

#Initialising dictionery
dict={}

#description about program
line() #Calling line function
print('\n')

timestamp() #Calling timestamp function
print("\n")   
des="Welcome!"
print(des.center(30,"'"))
des="\nthis is the program to generate serial number \n"
print(des.title())

line()
indes="\nIf you want Alpha numeric serial number then [press 'yes'] \nand for only numeric  number [press '0'] "
print(indes.title())

#Taking input from user 
c=input("\nEnter your response  :  ")

if "yes" in c:
     seral=input("Enter alphabet : ")
     serno=input("Enter number : ")
else:
     serno=input("Enter number : ")

sr= seral+serno
n=int(input("Enter limit : "))
line()
print("\n Your serial numbers are ...\n")
#calling funtion
serialno(n, sr)

#End line
line()
print("\nCopy and use as required....\n ")
end="Thank You!"
print(end.center(30,"'"))


