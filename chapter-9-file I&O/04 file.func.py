# for reading every lines "readlines ()"

f = open("file.txt.1")
lines = f.readlines()
print(lines)
f.close()

# for reading every line one by one " readline ()"

f = open("file.txt.1")
line1 = f.readline()
print(line1)
f.close()

# for append data to a file 
f = open("file.txt.1", "a")
f.write("This is a new line.\n")
f.close()

