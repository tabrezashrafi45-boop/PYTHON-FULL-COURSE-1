# conditional statements

# 01_if statement 

# checks only one condition 

a = int(input("enter your age:"))

if(a>=18):
    print("you are eligible") 
    # when we enter the age less than 18 ,then we use another statement

# 02_if-else statement

# checks more than one condition and uses both "if" and "else" statement

b = int(input("enter your age :-"))
if(b>=18):
    print("your are eligible ")  
else:
    print(" you are not eligible")

    # 03_if-elif-else statement
    # used for multiple condition 
    c = int(input("enter your age ::-"))
    if(c>=18):
        print(" you are eligible ")
    elif(c<0): # if i want to add any condition in a statement we use "elif"
        print("you are entering the non-valid age")
    else:
        print(" u are not eligible ")
        print("end of program")
    