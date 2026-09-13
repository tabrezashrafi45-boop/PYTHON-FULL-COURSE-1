# write a program to detect a spam message by following keywords 
# " make a lot of money " , "buy now" , "subscribe this" , "click this"

comment = input("enter your comment :-")
if(("make a lot of money"),("buy now"),("subscribe this"),("click this")):
    print("this is a spam")
else:
    print("this is not a spam")

    # OR we use "IN" operator in the program to detect all the spams

comment = input("enter your comment :-")
p1 =("make a lot of money")
p2 = ("buy now")
p3 =("subscribe this")
p4 = ("click this")

if((p1 in comment) or (p2 in  comment) or (p3 in comment) or (p4 in  comment) ):
    print("this message is a spam")
else:
    print("this is not a spam")