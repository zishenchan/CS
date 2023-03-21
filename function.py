'''
function is a mini-program you add on your code, easier to read, easier to understand

it only activates when it called, run all your code inside of your box(function),

the data you pass into your function code, it called parameters, parameter is not defined inside function

when you call the function, inside the parentheses, it called argument

argument will pass the value to parameter and assigned, and run code by this parameter

at the end, it can return data out of the box, by using return

return means when you called the function, you will have a return-result that assigned to this function
'''


# return difference
def text_string():
    print('it\'value output when call the function')
    return 'it\'return output for whole funciton'

y = text_string()
print(y)



def example(): # def is defining a function, which called 'example'
    print("This is function") # this is body of function, statement is 'print()' 
    #at front there is indentation
    print("example")

example(parameters) # you have to define it before you use the function, you can call it many of times
# inside bracket, parameters will give value to the function



def example(name): # 'name' will be executed at below 
    print("This is function",name) # once line 10,11 have been executed, it will go to line 14
    print("example")

example("Jack") # when we call function, "Jack" as an argument will pass to 'name' variable at example()




def example(num_1,num_2): # it accpects function call at line 34, num_1 and num_2 is assigned by 230 and 240 in line 32
    result = num_1 + num_2
    return result # return go back to where function is called
    # The return statement is used to exit a function and go back to the place from where it was called.
result = example(230,240) # once we call function, it passes to line 28 to execute
print(result) # once the function call is executed at line 34, there is value for 'result' and print it







print() # we don't have to define print function, because it is built-in function, already written it python
# built-in function included len(),sum() and so on



# recursive function
def factorial(x): # the value 2 will run again, return is 2*factorial(1),and run again, it return 0 at line 57
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1)) # equals to 3 * (3-1), factorial(2)will recurred line 55
'''there are three times return, at third times,return will be n=1. at second times, return will be
   (2* factorial(1)) / (2*1)
    at first times, return (3 * factorial(2)) / (3 * 2), final output will be 6
'''
num = 3
print(num,factorial(num)) # 3 is passed to line 55



#lambda function / anonymous function
double = lambda n:n*2 
'''lambada arguments : expression
it can only one expression, but can multiple arguments
'''
print(double(2)) # the output is 4 (2*2)



# local variables and global variables
num = 3 # assign 3 to num, it is global variable
def greet(n):
    n = 4    # global variable is changed to 4
    print("inside the function",n) # when the function end, this variable is destroyed
# try not to use global variables to inside function, it makes it reall hard to understand
greet(num) #  call the function greet
print("outside the function",num) # the variable 'num' is global variable



num = 3 # 3 is assigned to num
def greet():
    # use 'global num' to change global variable
    num = num + 1 # unbondlocalError,  glocal varaible can not change by inside function
    print(num)
greet() # call function greet




for list_2 in list_1: # list_1 is assigned to list_2 one by one, it's loop function
  print(list-2) # iteration of lists, output all element
print("Hello" in list_1) # output is True, boolean type
# if output contains empty line, because some elements in the file 
# ends with a special character that indicates the end of a line



# we use module to break down large program. The file name 'function.py' is called module
# (i.e 'import math',  math contains lots of mathematical function and constants)
import math # import module using 'import statement'
import math as m # python import modules also 'import math as m' rename the modules

from math import sin
'''also 'from math import sqrt,sin' you import operator
also custom modules, new operator.py file
def add(a,b):
    return a + b
create a new .py file to 'import operator.py'
'''
num = 25
result = math.sqrt(num)
result_1 = math.trunc(num)
result_2 = round(num)
print(result)


dir() # function to find out names that are defined inside a module.
