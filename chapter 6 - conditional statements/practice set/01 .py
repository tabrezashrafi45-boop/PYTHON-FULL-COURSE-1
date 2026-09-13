# WRITE A PROGRAM TO FIND THE GREATEST OF FOUR NUMBER ENTERD BY USER
a1 = int(input("enter your number :-"))
a2 = int(input("enter your number :-"))
a3 = int(input("enter your number :-"))
a4 = int(input("enter your number :-"))
if(a1>a2 and a1>a3 and a1>a4):
    print("a1  is the greatest  number ",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("a2  is the greatest  number ",a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("a3 is the greatest  number ",a3)
else:
    print("a4 is the greatest number",a4)

