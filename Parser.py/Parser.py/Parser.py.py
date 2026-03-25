input("Enter your file name:")
filename  = "Bee_Movie.txt"
file = open(filename, 'r')

line = file.readlines()
while line: 
    print(line)
    line = file.readline()

file.close()
