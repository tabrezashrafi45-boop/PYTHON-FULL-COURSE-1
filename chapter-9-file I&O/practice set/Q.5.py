# write a program to censor the following words from a file : donky, stupid, idiot

words = ["donkey", "stupid", "idiot"]
with open("file.txt.1","r") as file:
    content = file.read()
    for word in words:
        content = content.replace(word, "####")
with open("file.txt.1","w") as file:
    file.write(content ) 