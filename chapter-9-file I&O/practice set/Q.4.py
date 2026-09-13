# write a program to replace the word "donkey" with "####" from a file .
word = "donkey"
with open("file.txt.1","r") as file:
    content = file.read()
    contentnew = content.replace("donkey","####")
with open("file.txt.1","w") as file:
    file.write(contentnew)