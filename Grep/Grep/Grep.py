import glob 

file_name = input("Enter the file name: ")
pattern = input("Enter the pattern to search: ")    

file = open(file_name, "r")

line = file.readlines()

for i, in enumerate (lines): 
    if pattern in line:
        print(file_name, line.strip())


