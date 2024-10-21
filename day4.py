#day 4
#CHECK FORTUNE
m="WELCOME" #Greeting user
print(m.center(50))
mes="This program is for telling your fortune based on your birth date\n" #program description
print("\n", mes.title())

#Taking  input
n=int(input("Enter Your BIRTH DATE :  "))
print("\n YOUR FORTUNE IS....\n")

#Checking each  case to meet the condition
match n : 
    case _ if n>0 and n<=3:
       print("An unexpected opportunity to learn something new.")
    case _ if n>3 and n<=10:
       print("Finding peace in a quiet moment of reflection.")
    case _ if n>10 and n<=15:
       print("Tumhara kuch na ho payga .\n Ghar walo ko naya kar lene do .")
    case _ if n>15 and n<=20:
       print("Overcoming a challenge with newfound confidence.")
    case _ if n>20 and n<=25:
       print("Reconnecting with an old friend.")
    case _ if n>25 and n<=31:
       print("Gaining clarity on a difficult decision.")
    case _:  #default case for any unspecified input
       print("Janam Tarik bhi yaad nai tujhe \n Jaa baap se puch ke aa..")

mess="\nTHANK YOU"
print(mess.center(50))
             