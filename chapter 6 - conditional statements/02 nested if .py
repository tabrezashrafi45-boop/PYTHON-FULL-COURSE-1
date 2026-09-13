# "NESTED IF" OR "IF ELSE LADDER"
# NESTED IF means we use multple condition in a single program
# and that program pattern is called " IF ELSE LADDER"

marks = int(input("enter ur marks:-"))
if(marks<=40):
    print(" bad ")
elif(marks<=60):
    print("average ")
elif(marks<=80):
    print("good ")
else:
    print("excelllent")
    print("end")

    # MORE THAN ONE "IF" , "ELSE" , "ELIF" is used in one program but every "IF" has its own independent execution
    