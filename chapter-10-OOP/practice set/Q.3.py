''' 
# create a class attribute and then create another  object attribute and check that 
the original attribute is change or not . 
'''

class salary:
    salary = 3000

a = salary()
a.salary = 4000

print(a.salary)

# output 
''' output will be change'''