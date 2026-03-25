fname = "output.txt"
file = open(fname, 'a')
for i in range(10):
    file.write("This is the line {1}.\n")
file.close
    