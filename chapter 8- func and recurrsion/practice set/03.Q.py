# write a program to print the sum of natural number using recursive func
def sum(n):
   if(n==1):
      return 1
   return sum(n-1) + n
print(sum(8))
