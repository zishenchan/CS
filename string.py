# few ways of string concatenation
youtuber = "" # create a variable
print("The output is" + youtuber) # use '+' string
print("The output is {}".format(youtuber)) # use 'format' string with curly bracket
print(f"The output is {youtuber}") # use 'f' string with curly bracket



# multiple lines of strings
# use back slash
print("At its last meeting, the bank had warned that inflation would peak above 13%. \
  The bank said Thursday that the recently announced cap would likely mean consumer-price \
    rises will peak at just under 11% in October but inflation could remain in double digits for \
      months before falling. ")


# mutiple quote in string
# use backslash
print('you don\'t have fish') # the output will be 'you don't have fish


# about print built-in function space
print("My","place") # python will automatically leave space with comma bewteen
print("My name",  "is Sam") #no matter you leave space after comma, it still leave one space


# address of RAM
a = 2 # '2' is object stored in memory and 'a' is name
print(id(a)) # 'id' built-in function is for getting the address of RAM



# How to output decimal place and next line
# sep parameter used for insert between two strings
num = 2
print(f"This is two space {num:.2f}")
print("This is first string","This is second string",sep = "!!", end = "..")



for word in open("pride_and_prejudice.txt"): # use for loop struction iterate over txt file
  word_new = word.rstrip("\n") # stripped right side of strings with space(\n)
  word_new1 = word.lstrip("\n") # stripped left side of strings with space(\n)
  word_new2 = word.strip("n") # stripped "n" with txt file, not included in the middle of strings
  if len(word.rstrip("\n"))>=4: # the length of result of rstrip
    print("The length with space is over 4") # if string contains \n, it counts one space in len()
  print(word_new)


# check string value
print("a" in "cake")# check whether the value of left side is contained among in right side 
letter = "s" 
print(letter in "rose")# check the value of variable letter is contained among in string rose
word = "Superb"
print("p" in word)# check the string p is contained among in variable word



# use for loop struction iterate over txt file
for letter in open("pride_and_prejudice.txt"):
  
  if letter.__contains__("e") == False: # if letter contains "e" is false
    print(letter.rstrip("\n")) # print letter without space at right side
'''
we put \n at statement because use for loop insturction, the output contains new space line originally
we need to use rstrip function to delete it
'''



# startswith and endswith method
word = "persuasion" # string is assigned to word
if word.startswith("p"):# string method is 'variables.method(agruments)'
  print("There is a 'p' at the beginning.")
if word.endswith("p"):# value of variables ends with "p"
  print("There's a 'p' at the end.")



# use for loop struction iterate over txt file
for letter in open("pride_and_prejudice.txt"):
  if "a"in letter and "e"in letter and "i"in letter and "o"in letter and "u"in letter:
    # use 'and' opeartor to filter word without letter a,e,i,o,u
    # or we can use nested-if statement
    print(letter.rstrip("\n"))# print letter without right space



# rstrip method
for letter in open("pride_and_prejudice.txt"):# use for loop struction iterate over txt file
  if int(len(letter.rstrip("\n"))) >=3: # add rstrip to delete empty space line, otherwise len+1
    if letter[0].isupper():# check first element is uppercase
      print(letter.rstrip("\n"))
    else:
      print("   ",letter.rstrip("\n"))




