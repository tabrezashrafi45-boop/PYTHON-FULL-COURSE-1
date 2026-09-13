# write a program to find the factorial of any number using for loop

n = int(input("enter the number :-"))
product = 1
for i in range (1,n+1):
    product = product * i
print(f"factorial of {n} is {product}")  