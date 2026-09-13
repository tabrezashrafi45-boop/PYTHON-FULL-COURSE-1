# write a program to print the table of 2 to 20 and store it in a different file
import os

os.makedirs("tables", exist_ok=True)

def generate_table(n):
    table = ""
    for i in range (1,11):
        table += f"{n} X {i} ={n*i}\n"
    with open(f"tables/table_{n}.txt", "w") as file:
        file.write(table)

for i in range(2, 21):
    generate_table(i)


        
