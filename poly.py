m=input("do you have a medical cause Y or N")
a=int(input("enter you attendance"))
if m=="Y": 
   print("you are allowed")
else:
   if a>=75:
    print("younare allowed for the exams")
   else:
    print ("your not allowed for the exams")