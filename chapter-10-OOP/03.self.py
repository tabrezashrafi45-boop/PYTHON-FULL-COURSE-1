# SELF PARAMETER 

'''self is a reference  of the class.
It is used to access variables that belong to the class. 
It must be the first parameter of any function in the class.'''

# example of self parameter :
class employee:
   company = "Google"
   salary = 50000
   age = 25

 # we use self parameter here
   def info(self):
    print(f"the salary is : {self.salary}") 

    @staticmethod 

    # it is used to stop the self paameter from being passed.

    def greet(): # another self parameter 
      print("hello")

tabrez = employee()
tabrez.salary = 60000
#employee.info(tabrez)  # recall the func
  # recall the func (2nd self parameter)
tabrez.info()



