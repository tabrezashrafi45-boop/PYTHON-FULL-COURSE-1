# write a program to find the grade of the student
grade = int(input("enter your grade:-"))
if(grade>=90 and grade<=100):
    print("excellent")
elif(grade>=80 and grade<=90):
    print("A")
elif(grade>=70 and grade<=80):
    print("B")
elif(grade>=60 and grade<=70):
    print("C")
elif(grade>=50 and grade<=60):
    print("D")
elif(grade<=50):
    print("FAIL")
