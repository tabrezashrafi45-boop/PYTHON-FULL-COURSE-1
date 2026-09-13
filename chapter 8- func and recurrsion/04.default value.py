''' "DEFAULT VALUE " is used for printing the default value when ending or starting 
input is not given '''

# EXAMPLE
def goodDay (name,ending = "thank you"):
    print("goodDay",name)
    print(ending)
goodDay("tabrez","thanks")


 # "ending" = thanks , when we give the value of ending it prints the given value 
 # OUTPUT :-
'''goodDay tabrez
thanks'''


 # but when we not give the value of ending it prints the default value 
goodDay("rohan")
# OUTPUT:-
'''goodDay rohan
thank you'''