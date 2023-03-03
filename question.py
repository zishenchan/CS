# question 01
# assignment 1 name question
# default input is Lucas1, Lucas2, Lucas Hello

'''
my problem is I use the .replace() method to check whether in alphabet,
however the final output can not be the original input,
for third input, final variable will be LucasHello (without blank space)
'''

# method 01
name = str(input("Please enter your name: "))
name = name.replace(" ","") # replace method for blank space
while name.isalpha()==False: # isalpha function checks whether a character is an alphabet or not
    print("Error: Only accept alphabetical characters and spaces for name\n")
    name = str(input("Please enter your name: "))
    name = name.replace(" ","")

# method 02
name = str(input("Please enter your name: "))
for x in name: # x is assigned letters one by one
    if x.isspace(): # check whether string has blank space
        name_new = name.replace(" ","") # if yes, make it without blank space, and check alphabet
        if name_new.isalpha():
            print("done")
            break
        else:
            print("error: Only accept alphabetical characters and spaces for name\n")
            name = str(input("Please enter your name: "))
    else:
        if x.isalpha():
            print("done")
            break
        else:
            print("Error: Only accept alphabetical characters and spaces for name\n")
            name = str(input("Please enter your name: "))



#question 02
str_1 = "He said \"what\'s your phone number?\"" 
# if string contains quotation mark, put back slash in front of quo?


# question03
# isinstance function
c = 5 + 3j
print(c + 3)
print(isinstance(c,complex))



# question 04
'''
there is a difference bewteen if function and if-else function 
if we do not put 'else', the output will loop more than one
'''
# if-else function
def showNumbers(limit):
    
    for x in range(0,limit+1):
        if x % 2 == 0:
            print(f"{x}","EVEN")
        else:
            print(f"{x}","ODD") 

showNumbers(int(input()))

# if function
def showNumbers(limit):
    
    for x in range(0,limit+1):
        if x % 2 == 0:
            print(f"{x}","EVEN")
        print(f"{x}","ODD") 

showNumbers(int(input()))
