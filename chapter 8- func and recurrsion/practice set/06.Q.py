# write a program to build a multiplication table using
def multiply(n):
    if (n==0):
        return 
    for i in range (1,11) :
        print(f"{n} X {i} = {n*i}")

multiply(5)