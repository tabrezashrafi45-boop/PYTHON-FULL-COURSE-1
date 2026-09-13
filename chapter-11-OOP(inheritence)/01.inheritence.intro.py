# INHERITANCE 
''' inheritence is a way of creating a new class for using details of pre- class without modifying it.

 The newly formed class is a derived class (or child class). The existing class is a base class (or parent class).'''


class employee:    # base class(parent class)
     company ="google"
     def show(self):
          print(f"the name of company is {self.company}")

class programmer (employee):   # derived class (child class)
     language = "python"
     def showlanguage (self):
          print(f"the name of company is {self.company} and the programmer is best in : {self.language}")

a = employee()
a.show()
b = programmer()
b.show()
b.showlanguage()