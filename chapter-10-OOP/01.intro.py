# Introduction to Object-Oriented Programming in Python

''' solving problems using classes and by creating objects is called Object-Oriented
 Programming (OOP). 
 
 OOP is a programming  that uses "objects" to design applications and computer programs.
 
 It utilizes several techniques like including modularity, 
 polymorphism, and encapsulation.'''

# class definition
'''A class is a blueprint for creating objects. 

It defines a set of attributes and methods that the created objects will have.'''

# program of class 
  
class employee:
    name = " tabrez"
    age = 25
    salary = 50000

    print("Employee Name:", name)
    print("Employee Age:", age)
    print("Employee Salary:", salary)


    # this is the basic exxample of class .


    # OBJECTS
    '''An object is an instance of a class.
     
       It is created from the class blueprint and can have its own unique values for 
       the attributes defined in the class.'''

    # class attributes
    '''Class attributes are variables that are directly belongs to their particular class.
      
      example:
      class employee:
    name = " tabrez"
    age = 25
    
    here name and age are the class attributes.'''

    # instance attributes / object attributes
    '''Instance attributes are variables that are specific to each instance of a class.
     
      example:
      class employee:
          salray = 50000
          age = 25
          tabrez.name =" md shamsh tabrez"

          here tabrez.name is the instance attribute because it does not belong to the class.
            
          # instance attributes takes precedence over class attributes.'''   


