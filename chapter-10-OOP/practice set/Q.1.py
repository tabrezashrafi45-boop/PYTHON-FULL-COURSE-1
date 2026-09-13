# write a program for creating a class programmer who are working for microsoft.

class programmer :
    company ="microsoft"
    def __init__(self,name ,language ,salary):
        self.name = name
        self.language = language
        self.salary = salary

p = programmer("tabrez","python", 100000)
print(f"the name of the programmer is {p.name}.and his speciality is {p.language}.and his salary is {p.salary}. ")
    