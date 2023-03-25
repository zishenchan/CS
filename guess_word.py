# we guess number from computer
import random
def guess_number(n):
    # return a random integer between (a,b)
    num = random.randint(1,range_number) 
    while n != num:
        if n < 1 or n > range_number:
            print("Sorry, please input a valid number: ")
            n = int(input("Guess a number again: "))
        elif n > num:
            print(f"Sorry, your number {n} is larger, try again")
            n = int(input("Guess a number again: "))
        elif n < num:
            print(f"Sorry, you number {n} is smaller, try again")
            n = int(input("Guess a number again: "))
        
    print("Congrats, you guess the correct number")

range_number = int(input("Set the number range begin with 1 : "))
guess_number(int(input(f"Guess a number bewteen 1 to {range_number}: ")))