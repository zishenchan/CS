'''
terminal is a interface that you can interact with your computer's command line

we use VS studio as code editor, and we set up a folder on our computer and create file and write code inside

often use terminal to execuate your code
'''


# python difference from math
from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE
from pkg_resources import add_activation_listener

'''
print(1.1 + 2.2 == 3.3)
output is False
floating-point numbers are implemented in computer hardware as binary fractions 
as the computer only understands binary (0 and 1). 
Due to this reason, most of the decimal fractions we know, 
cannot be accurately stored in our computer.
'''



# integer
# numerical datatypes
10000,12



# float - have decimal value
1. # equal 1.0
4000.00



# boolean 
True
False



# string - with single or double quotes
"Hello World"
'Hi'




'''
ordered collection : 'list' and 'tuples'
unordered collection : 'set' and 'dictionary'
'''
# list is a collection of values with specific order

list_1 = ["Here","is","list"] # list uses square blacket
list_2 = ["Here","is","difference",29] # list is ordered sequence of items, do not need to be same types

list_1[1:2] = ["890","8656"] # assign the new element
list_1.append("Youtube") # append methods, insert this element at the end of squence
list_1.insert(1,"Youtube") # this element will be the second elements of list_1
list_1.remove("Hello") # remove the elemnt
list_3 = list_1.copy() # print list_3, will be the copy of list_1
print(len(list_1)) # for counting the numbers of integers in squence list_1
print(list_1[0]) # first element is 0, if there are 3 elements and print(list_1[3]), will be indexError
# if use negative index, the last element is [-1], the thired element from the last [-3]
print(list_1[1:3]) # not include element [3]
print(list-1[:3]) # is equivalent to [0:3]
print(list-1[2:]) # will output till the last element
list_1.sort()# output will be ['a', 'b', 'c', 'e'], sort in alphabetical order
list_2.sort(key = lambda x:len(x))# output will be ['ab', 'abc', 'abcdefg'], sort by length



# tuples is a collection of values with specific order, but immutable
tuples_1 = (5,"program") # Tuple is ordered sequence of items like list, but it is immuteable, once created, cannot be modified



# set a collection of values unordered and does not allowed duplicates
countries = {"China","USA"} # for set, it uses curly blacket
print(countries) # output is not in order, even there are two same elements, still output one
countries.add("Japan") # add element to set

countries = {"China","USA"} 
countries_1 = {"Japan","Russia"}
countries_1.update(countries,{"UK"}) # countries_1 became union of set(countries and countries_1)
# behind the comma is adding another element




# dictionary a collection of unordered key--value pairs
d = {1:"dictioary",2:"dic"} # dictionary is unordered collection of key-value pairs
# the pair form will be 'key:value'



name_2 = ["23","890"]
print(set(name_2)) # it can convert list to set



# operator 
+ # addition 
- # subtraction
** # to the power of ...
= # assign 
!= # does not equal


# membership operator
1 in [1,2] == True
1 not in [1,2] == False


# variable is a stored memory that can be changed in the future
# declear a variable by '='
# capical matter when you assign a variable
'''
for mutable datatype, you can edit on variable, can use append method
i.e. list and dictionary is mutable datatype, list_1 = [1,2,3] in memory, value is stored by '1' '2' '3', so you can change it 
if you change value of index[0], the one that same value assigned with different variable name will be change also
'''

'''
for immutable datatype, you can not edit and make change
i.e. tuples and string is ummutablbe datatype, tuples[1] = 2 will be typeerror, string will create another one
'''







