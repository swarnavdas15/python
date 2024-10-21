#Day6 
#Greeting program
import time as t

#Printing program details
mes="welcome to this program"
mes=mes.upper()
print(mes.center(50))
print("This Program Is To Greet User With Timestamp!\n\n")

#Internal execution of extracting and storing current time
time=t.strftime('%H:%M %p')
H=int(t.strftime('%H'))

#Greeting user with a message
if (H>=6) & (H<12):
    print("GOOD MORNING SIR! \nItS->", end=" ")
    print(time , "\n HAVE A GOOD DAY AHEAD !")
elif(H>=12) & (H<16):
    print("GOOD AFTERNOON SIR! \nItS-> " , end=" ")
    print(time , '\n HAVE A BREAK SIR !')
elif(H>=16) & (H<21):
    print("GOOD EVENING SIR! \nItS-> " , end=" ")
    print(time , '\n ENJOY YOUR TIME SIR !')
else:
    print("GOOD NIGHT SIR! \nItS-> ",  end=" ")
    print(time , '\n HAVE A GOOD SLEEP !')