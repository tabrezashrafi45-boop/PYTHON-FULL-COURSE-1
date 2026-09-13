# 01 :- string slicing means we can make the part of the strings
 
 
# 02 :- string are can't change if they are made once means string are immutable

# 03 :- STRING LENGTH :- Numbers of alphabets or digits are called its lenght
name = "tabrez"
print(len(name)) # lenght = 6

# 04 :- counting the lenght of the string 
 # starts with "0123.... and so on"
 # and negative side "so on ......,-4,-3,-2,-1"


# 05 :- finding the slicing parts of string 
name = "tabrez" 
nameshort = name[0:3] # means starting with "0" and ending at "2 " not at "3"
print(nameshort)

# special cases 
name = "tabrez" 
nameshort = name[:3] # means starting with "0" 
print(nameshort) 

name = "tabrez" 
nameshort = name[1:] # means ending with the lenght of the strng "6" 
print(nameshort)

# SLICING with skip value 
name = " md shamsh tabrez" 
nameshort = name[1:6:3] # means starting with "1" to "5" then skip every third place 
print(nameshort)




