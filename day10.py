#Day 9
#Koun Banega Carorepati

import time  as t  #importing time module to print timestamp

# Description of program

def des():
      #describing function
      des="\n\t\t\tWelcome!\n\n\tthis is the program for quiz game...\nDeveloped by - 'Swarnav Das'"
      print(des.title())
      line()
      try:
              nam=input("\nEnter Your Name : ")
      except:
              print("Invalid Input")
      #greting user 
      des='\nHello {} ...\nChaliye Shuru krte kismat ka khel '
      print(des.format(nam))
      line()

      des="\tKoun Banega Crorepati !"
      print(des.title())

# Timestamp in program

def timestamp():
        line()
        print(t.ctime()) #print date & time 

        count=int(t.strftime("%H"))

        match count:   #greeting user accordingly
              case _ if count>=6 and count<12:
                    print("\nGOOD MORNING SIR!")
                    print("WISHING YOU A ERROR FREE DAY AHEAD ...")
              case _ if count>=12 and count<=16:
                    print("\nGOOD AFTERNOON SIR!")
                    print("ENJOY YOUR MEAL AND KEEP CODING...")
              case _ if count>=16 and count<23:
                    print("\nGOOD EVENING SIR!")
                    print("HAVE A BREAK ...")
              case _ if count>=23 and count<6:
                    print("\nGOOD NIGHT SIR!")
                    print("HAVE GOOD SLEEP...")

# Decoration line

def line():
       for val in range(60):
                print("-",end="")
       print("\n")

# Question library

def questionlib (n):
        ques=["A. Who is the developed Python ?", "B. Who among the following considered as the 'father of artificial intelligence'? ", "C. Which was the world's first successful electronic computer ?","D. Who among the following used the term computer worm for the first time ?","E. Who was the fist Prime Minister of India ?", "F. G-20 Summit held on which city of India ? ", "G. Film 'RRR' got oscar for which song ? ","H. What is the name of our Galaxy ? ","I.Who is the father of Atom Bomb ? ","J. Who developed this program ?  "]
        ans=["Guido Van Rossum", "John McCarthy"," ENIAC","John Brunner","Jawahar Lal Nehru" ,"New Delhi","Natu Natu", "Milky Way", "J. Robert Oppenheime", "Swarnav Das" ]

        for i in range(len(ques)):
                   dict.update({ques[i]:ans[i]}) #updating question dictionary

        print(ques[n], "\n")
        answ=dict.get(ques[n])
        quesa=ques[n] 
        ck=option(quesa,answ,n)
        
        if ck == 1:    #returning value to make continue the question loop
            return 1
        else:
            return 0 
        
# Option collection       
      
def collection():
   col={"Roni", "Swarnav", "none", "Baigan", "Puja ", "Rekha Se Puch", "Binod", "Robert Nalla" , "Thala", "Mc John","Albert", "Jhonny","Goa","Thailand", "Anuradha", "Jetha lal "}
   #set of options to get random option order
   temp=[] #temporary list
   for val in col:
      temp.append(val)
   
   return set(temp[:3]) #returning random option as list

# Consent to continue

def consent():
      try: #taking consent from user to continue
            con=input("Do want to continue \n[ Enter Yes : To continue...\nEnter 0 : To exit... ]:  ")
            if con == "yes":
                return 1  #if consent is valid return 1
            else:
               return 0
      except:
            return  0
      
# Display option and take respose

def option (ques, answ, r):
       optn=collection()  #calling option collection to get random options
       optn.add(answ)
       list=[] #initialising temporary list
       
       for val in optn:    #adding options in temporary list
                 list.append(val)

       for i in range (2):   #listing options
             if i==0:
                    print(i+1,".", list[i], "\t\t\t\t", i+2,".", list[i+1])
             else:
                    print(i+2,".", list[i+1], "\t\t\t\t", i+3,".", list[i+2])
              
       n=int(input("\nEnter Your Respose : "))  #taking response of option
       line()
       try:    #handling error if occurs
               val=list[n-1]     
       except:
               print("Enter valid option !")
               return 0

       ck=response(ques, val ,r)
       #fetch response nature
       if ck == 1:
                return 1   
       else:
                return 0

# Check weather response is correct or not

def response (ques, val , r):
         temp = dict.get(ques)
         #check question answer pair in dictionary
         if temp == val:
                 print("Sahi Jawab..\n")
                 return 1    #return 1 if response is correct 
         else:
                print("Galat Jawab..\n")
                return 0     #return 0 if response is incorrect
         
# Reward for correct answer         

def reward(n):
   rew=[1000,3000,5000,10000,20000, 40000, 80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
   return rew[n] #return reward assosiated to question
       
#Initialising dictionary     

dict={}

bal=0
timestamp()  #calling timestamp function
line()       #calling line function
des()        #calling description function

for i in range (10):
   line()
   n = questionlib(i)   #calling question library
   
   if n==1:
          line()
          rew= reward(i)
          des="\nMubarak Ho App Jittey ho {} Ruppey..."
          print(des.format(rew))
          line()
          bal+=rew 
          con=consent()
          line()
          if con == 0:
                break      #if consent fails or  response is NO,  then program BREAKS   
   else:
          line()
          break
   
# Balance after ending the quiz is displayed

des="Toh aaj app yha se le jate hai Rs.{} ...\nUmeed Hai Aap Yeh Dhan-Rashi Achhi Jagah Kharcha Krenge ..."
print(des.format(bal))
line()
end="Thank You ..."
print(end.center(50," "))
print("Credit-'Puja Chakraborty'")
   