# write a program to find out the number is prime or not
num = int(input("enter the number "))
for i in range(2, num): # means "num" is divided by 2 number atleast
    if(num%i) == 0:
        print("number is not prime")
        break # we use break statement for exit the loop when number is not a prime
else:
     print("number is prime") # this "else " is used for "for loop" not for "if".