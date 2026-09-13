# write a program to test the student result a/c their result > 40% overall AND > 33% in one subject
marks1 = int(input("enter the marks :-"))
marks2 = int(input("enter the marks :-"))
marks3 = int(input("enter the marks :-"))

total_percentage = (100*(marks1 + marks2 + marks3))/300
if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("congrats ! , you are pass",total_percentage)
else:
    print("sorry , you are fail ",total_percentage)