# let computer guess your secret number


import random
def computer_guess():
    
    # set the range
    low_number = int(input(f"Set a low number "))
    end_number =int(input(f"Set a end number to make range bewteen {low_number} to ? "))
    print(f"Computer will guess a number between {low_number} to {end_number}")
    
    # use dynamic number range by changing the low and high
    num = random.randint(low_number,end_number)
    feedback = str(input(f"Is {num} correct or high / low? type(c/h/l): "))
    feedback = feedback.lower() # aviod user input uppercase letter

    # make the loop
    while True: 
    
        if feedback == "c": 
            break
        elif feedback == "h":
            end_number = num - 1
            num = random.randint(low_number,end_number)
            feedback = str(input(f"Is {num} correct or high / low? type(c/h/l): "))
            feedback = feedback.lower()
        elif feedback == "l":
            low_number = num + 1
            num = random.randint(low_number,end_number)
            feedback = str(input(f"Is {num} correct or high / low? type(c/h/l): "))
            feedback = feedback.lower()

    # print the output        
    print(f"yeah! Your computer successfully guess your number {num} correctlly")

computer_guess()
