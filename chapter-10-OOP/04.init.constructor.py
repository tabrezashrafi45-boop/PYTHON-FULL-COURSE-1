# __init__()
''' The __init__ method is a special method in Python classes that is automatically called
 when an object of the class is created. 
 
 It is used to initialize the attributes of the object.
  
it is also called the constructer. '''

# example of __init__ method :
class employee:
   company = "Google"
   salary = 50000
   age = 25

   # init method 
   def __init__(self): # it is auto recalled because it is also called dunder method.
    print ("i am a invicible")
 
   def info(self):
    print(f"the salary is : {self.salary}") 
tabrez = employee()
tabrez.salary = 60000
tabrez.info()

