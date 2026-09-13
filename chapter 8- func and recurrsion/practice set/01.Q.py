# write the program to find the greatest of three number

def greatest(a,b,c):
    if(a>b and a>c ):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a = int(input("enter the number 1 :-"))
b = int(input("enter the number 2 :-"))
c = int(input("enter the number 3 :-"))
print(greatest(a,b,c))
