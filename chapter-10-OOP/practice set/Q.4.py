# add a static method to 2nd question and greet the user 
class calculater:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"the square of {self.number} is {self.number * self.number}")

      

    def cube(self):
        print(f"the cube of {self.number} is {self.number * self.number * self.number}")

    def squareroot(self):
        print(f"the squareroot of {self.number} is {self.number ** 0.5}")

    @staticmethod
    def hello():
        print("hello there is ")
a = calculater(9)
a.hello()
a.square()
a.cube()
a.squareroot()