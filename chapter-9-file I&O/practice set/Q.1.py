'''
 write a program to read the poem from a file and find the word twinkle  that
    it is in the poem or not.
   '''
f = open("file.txt.1")
line = f.read()
if ("twinkle" in line):
    print("The word twinkle is present in the poem.")
else:
    print("The word twinkle is not present in the poem.")
f.close()


