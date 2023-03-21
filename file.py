try:
    f = open('message.txt','r') # open file in same directory, it represents file 
    # 'r' represents read mode, w for write, a for append
    contant = f.read(6) # only first 6 characters will be printed
    print(contant)
finally:
    f.close() # it will always close the file, otherwise using 'with as' syntax



with open('message.txt','r') as f:

    contant = f.read(6) 
    print(contant)
    f.close()
    # it will automatically close the file, using 'with as' mathod


with open('python.txt','w') as f:
    f.write("I love python")
    f.write("python is best")
    # when you run this program, in this directory, file is created, and called' python.txt'


with open('python.txt','a') as f: # 'a' for append content in file
    f.write("\npython is best language")

# there are many method (i.e) read(4) means read first 4 character. readline()
    

