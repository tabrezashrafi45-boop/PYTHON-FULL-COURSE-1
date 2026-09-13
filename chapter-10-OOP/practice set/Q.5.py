# write a program to get the ticket for a railway where fsir and seat availability is shown.
from random import randint

class train:

    def __init__ (self, trainNo):
        self.trainNo = trainNo

    def book(self):
        print(f"Ticket is booked in train of train no: {self.trainNo}")

    def getstatus(self):
        print(f"the train of train no {self.trainNo} is  running on time ")

    def getfair(self):
        print(f"the fair of the train {self.trainNo} is {randint(250,5000)}")

t = train(12204)
t.getstatus()
t.getfair()