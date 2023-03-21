
'''
07 Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
'''
def prime_number(num):
    for x in range(0,num+1):
        if x % 2 == 1 and x % 1 == x:
            print(x)

prime_number(int(input()))


# calculate the sum of 1+2+3+...+100
num = int(input())
result = sum(range(num,101))
print(result)



# loop function to list and sum the list
'''
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
'''
list_1 = []
def num(n):
    for x in range(0,n+1):
        if x % 3==0 or x % 5 ==0:
            list_1.append(x)

num(int(input()))
print(sum(list_1))





# example of function

def is_reverse(word1,word2):
    while len(word1)==len(word2):
        num = int(len(word2)-1)
        if word1[0]==word2[num]:
            print('is reverse')
        else:
            num -= 1
            break
    else:
        print('words are not equal number')

            
def add_element(x):
    total = [25]
    for a in x:
        total.append(a) # add element into list
    return total



def string_convent(x):
    if type(x)== str:
        list_string = list(x) # convent string to list by each character
        return list_string
    else:
        return print('this is not string, type again')


def alised_object():
    a = [0,34,13]
    b = a # more than 2 reference associated with object [0,34,13], it is alised object
    a[0] = 14
    print(b)


def character_count(x):
    d = dict()
    for c in x:
        if c not in d:
            d[c]=1 # create key c with initial value 1
        else:
            d[c]+=1
        return d


# try to avoid input is less than 0 with input variable a,b in the row, 
# value error is for everytime input a wrong number and output invalid
try:
    a = input('Enter a width: ')
    a = float(a)
    if a<0:
        print('Invalid!')
    else:
        b = input('Enter a height: ')
        b = float(b)
        if b<0:
            print('Invalid!')
        else:   
            result = a*b
            print('Area:',result)
except ValueError:
    print('Invalid!')