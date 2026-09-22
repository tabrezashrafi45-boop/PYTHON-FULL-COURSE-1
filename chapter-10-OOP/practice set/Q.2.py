# write a class "calsulator " hwich is able to find the square , cube and squareroot of a number.
class calculater:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"the square of {self.number} is {self.number * self.number}")
    def cube(self):
        print(f"the cube of {self.number} is {self.number * self.number * self.number}")
    def squareroot(self):
        print(f"the squareroot of {self.number} is {self.number ** 0.5}")
a = calculater(9)
a.square()
a.cube()
a.squareroot()
