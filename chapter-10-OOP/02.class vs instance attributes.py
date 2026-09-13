class employee:
   company = "Google"
   salary = 50000
   age = 25
tabrez = employee()
tabrez.salary = 60000

print("Employee Salary:", tabrez.salary)
print("Employee Age:", tabrez.age)

# output:
'''
Employee Salary: 60000     # here salary will be 60000 because  instance attributes are 
                             are precedence over class attributes.
Employee Age: 25

'''