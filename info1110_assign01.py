'''
Author: Zishen CHEN
SID: 510029106
Unikey: zche4727
'''
# time: 07/09 2022
name = str(input("Please enter your name: "))
name = name.replace(" ","") # replace two blank space
while name.isalpha()==False: # isalpha function checks whether a character is an alphabet or not
    print("Error: Only accept alphabetical characters and spaces for name\n")
    name = str(input("Please enter your name: "))
    name = name.replace(" ","")

    


age = int(input("\nPlease enter your age: "))
while age <0 or age >100: # check invaild input until goes to next step
    print("Error: The age is a number between 0 to 110")
    age = int(input("\nPlease enter your age: "))

times = float()   
if age >= 80: # calculate the times that fits the particular age group
    times = 0.6 - (age - 80) * 0.04
    if times <0.2:
        times = 0.2
elif age >= 75 and age <80:
    times = 0.75 - (age - 75) * 0.03

elif age >= 65 and age <75:
    times = 0.95 - (age - 65) * 0.02

elif age >= 60 and age <65:
    times = 0.99 - (age - 60) * 0.01

elif age < 60:
    times = 1

import math # math.ceil is a method rounds a number UP to the nearest integer. eg. if output 7.2, than will be 8
sum_1 = 15 * times
sum_2 = 20 * times
sum_3 = 10 * times
sum_4 = 10 * times
sum_5 =10 * times
sum_6 = 15 * times
sum_7 = 10 * times
sum_8 = 10 * times
sum_9 = 10 * times
plan_fat_loss = str(f'''Plate thrusters ({math.ceil(sum_1)} reps x 3 sets)
Mountain climbers ({math.ceil(sum_2)} reps x 3 sets)
Box jumps ({math.ceil(sum_3)} reps x 3 sets)
Lunges ({math.ceil(sum_4)} reps x 3 sets)
Renegade rows ({math.ceil(sum_5)} reps x 3 sets)
Press ups ({math.ceil(sum_6)} reps x 3 sets)
Treadmill ({math.ceil(sum_7)} mins x 3 sets)
Supermans ({math.ceil(sum_8)} reps x 3 sets)
Crunches ({math.ceil(sum_9)} reps x 3 sets)''')

sum_21 = 2 * times
sum_22 = 2 * times
sum_23 = 2 * times
sum_24 = 3 * times
sum_25 = 2 * times
sum_26 = 2 * times
sum_27 = 2 * times
sum_28 = 2 * times
sum_29 = 2 * times
plan_relax = str(f'''Quad stretchs ({math.ceil(sum_21)} mins x 3 sets)
Hamstring stretchs ({math.ceil(sum_22)} mins x 3 sets)
Chest and shoulder stretchs ({math.ceil(sum_23)} mins x 2 sets)
Upper back stretchs ({math.ceil(sum_24)} mins x 2 sets)
Biceps stretchs ({math.ceil(sum_25)} mins x 2 sets)
Triceps stretchs ({math.ceil(sum_26)} mins x 3 sets)
Hip flexors ({math.ceil(sum_27)} mins x 3 sets)
Calf stretchs ({math.ceil(sum_28)} mins x 3 sets)
Lower back stretchs ({math.ceil(sum_29)} mins x 3 sets)''')  

sum_31 = 20 * times
sum_32 = 20 * times
sum_33 = 20 * times
sum_34 = 30 * times
sum_35 = 20 * times
sum_36 = 20 * times
sum_37 = 15 * times
sum_38 = 15 * times
sum_39 = 15 * times
plan_high_intensity = str(f'''Jumping jacks ({math.ceil(sum_31)} reps x 4 sets)
Sprints ({math.ceil(sum_32)} reps x 3 sets)
Mountain climbers ({math.ceil(sum_33)} reps x 4 sets)
Squat jumps ({math.ceil(sum_34)} reps x 4 sets)
Lunges ({math.ceil(sum_35)} reps x 3 sets)
Crunches ({math.ceil(sum_36)} reps x 3 sets)
Treadmill ({math.ceil(sum_37)} mins x 2 sets)
Side planks ({math.ceil(sum_38)} reps x 3 sets)
Burpees ({math.ceil(sum_39)} reps x 3 sets)''')

sum_41 = 10 * times
sum_42 = 12 * times
sum_43 = 10 * times
sum_44 = 10 * times
sum_45 = 10 * times
sum_46 = 10 * times
sum_47 = 15 * times
sum_48 = 20 * times
plan_legs = str(f'''Back squats ({math.ceil(sum_41)} reps x 5 sets)
Hip thrusts ({math.ceil(sum_42)} reps x 3 sets)
Overhead presses ({math.ceil(sum_43)} reps x 5 sets)
Rack pulls ({math.ceil(sum_44)} reps x 5 sets)
Squats ({math.ceil(sum_45)} reps x 4 sets)
Dumbbell lunges ({math.ceil(sum_46)} reps x 3 sets)
Leg curls ({math.ceil(sum_47)} reps x 3 sets)
Standing calf raises ({math.ceil(sum_48)} reps x 2 sets)''')

sum_51 = 12 * times
sum_52 = 15 * times
sum_53 = 15 * times
sum_54 = 15 * times
sum_55 = 12 * times
sum_56 = 15 * times
sum_57 = 15 * times
sum_58 = 12 * times
sum_59 = 10 * times
plan_ABS = str(f'''Cross crunchs ({math.ceil(sum_51)} reps x 3 sets)
Knee ups ({math.ceil(sum_52)} reps x 5 sets)
Hip thrusts ({math.ceil(sum_53)} reps x 3 sets)
Mountain climbers ({math.ceil(sum_54)} reps x 3 sets)
Vertical hip thrusts ({math.ceil(sum_55)} reps x 3 sets)
Bicycles ({math.ceil(sum_56)} mins x 2 sets)
Front planks ({math.ceil(sum_57)} mins x 3 sets)
Dragon flags ({math.ceil(sum_58)} reps x 4 sets)
Reverse crunches ({math.ceil(sum_59)} reps x 3 sets)''')

sum_61 = 10 * times
sum_62 = 10 * times
sum_63 = 12 * times
sum_64 = 15 * times
sum_65 = 15 * times
sum_66 = 10 * times
sum_67 = 15 * times
sum_68 = 10 * times
sum_69 = 10 * times
plan_arms = str(f'''Bench presses ({math.ceil(sum_61)} reps x 5 sets)
Triceps dips ({math.ceil(sum_62)} reps x 5 sets)
Incline dumbbell presses ({math.ceil(sum_63)} reps x 3 sets)
dumbbell flyes ({math.ceil(sum_64)} reps x 3 sets)
Triceps extensions ({math.ceil(sum_65)} reps x 3 sets)
Pull ups ({math.ceil(sum_66)} reps x 5 sets)
Treadmill ({math.ceil(sum_67)} mins x 2 sets)
Bent over rows ({math.ceil(sum_68)} reps x 5 sets)
Chin ups ({math.ceil(sum_69)} reps x 3 sets)''')

sum_71 = 20 * times
sum_72 = 10 * times
sum_73 = 10 * times
sum_74 = 12 * times
sum_75 = 10 * times
sum_76 = 10 * times
plan_maleless18 = str(f'''High knees ({math.ceil(sum_71)} reps x 3 sets)
Squats ({math.ceil(sum_72)} reps x 3 sets)
Calf raises ({math.ceil(sum_73)} reps x 3 sets)
Scissor jumps ({math.ceil(sum_74)} reps x 3 sets)
Burpees ({math.ceil(sum_75)} reps x 3 sets)
Treadmill ({math.ceil(sum_76)} mins x 2 sets)''')



sum_81 = 20 * times
sum_82 = 18 * times
sum_83 = 12 * times
sum_84 = 15 * times
sum_85 = 10 * times
sum_86 = 15 * times
sum_87 = 12 * times
sum_88 = 10 * times
plan_maleover18 = str(f'''Standing biceps curls ({math.ceil(sum_81)} reps x 3 sets)
Seated incline curls ({math.ceil(sum_82)} reps x 3 sets)
Seated dumbbell presses ({math.ceil(sum_83)} reps x 3 sets)
Leg presses ({math.ceil(sum_84)} reps x 3 sets)
Bench presses ({math.ceil(sum_85)} reps x 4 sets)
Tricep kickbacks ({math.ceil(sum_86)} reps x 3 sets)
Hip thrusts ({math.ceil(sum_87)} reps x 3 sets)
Seated rows ({math.ceil(sum_88)} reps x 4 sets)''')



sum_91 = 20 * times
sum_92 = 18 * times
sum_93 = 12 * times
sum_94 = 15 * times
sum_95 = 10 * times
sum_96 = 15 * times
sum_97 = 12 * times
sum_98 = 10 * times
plan_femaleless18 = str(f'''Standing biceps curls ({math.ceil(sum_91)} reps x 3 sets)
Seated incline curls ({math.ceil(sum_92)} reps x 3 sets)
Seated dumbbell presses ({math.ceil(sum_93)} reps x 3 sets)
Leg presses ({math.ceil(sum_94)} reps x 3 sets)
Bench presses ({math.ceil(sum_95)} reps x 4 sets)
Tricep kickbacks ({math.ceil(sum_96)} reps x 3 sets)
Hip thrusts ({math.ceil(sum_97)} reps x 3 sets)
Seated rows ({math.ceil(sum_98)} reps x 4 sets)''')

sum_101 = 15 * times
sum_102 = 12 * times
sum_103 = 12 * times
sum_104 = 15 * times
sum_105 = 10 * times
sum_106 = 10 * times
sum_107 = 12 * times
sum_108 = 10 * times
plan_femaleover18 = str(f'''Lateral raises ({math.ceil(sum_101)} reps x 3 sets)
Reverse flyes ({math.ceil(sum_102)} reps x 3 sets)
Hip thrusts ({math.ceil(sum_103)} reps x 3 sets)
Incline dumbbell presses ({math.ceil(sum_104)} reps x 3 sets)
Squats ({math.ceil(sum_105)} reps x 4 sets)
Dumbbell lunges ({math.ceil(sum_106)} reps x 3 sets)
Leg presses ({math.ceil(sum_107)} reps x 3 sets)
Dumbbell presses ({math.ceil(sum_108)} reps x 4 sets)''')

 
sex = str(input("\nPlease enter your biological sex (female/male): "))

while (sex == "male" or sex == "female")==False:
    print("Error: Please enter valid input\n")
    sex = str(input("Please enter your biological sex (female/male): "))
else:
    print('''\nWhat do you want to get out of your training? 
    1. Your goal is losing weight
    2. Your goal is to staying calm and relax
    3. Your goal is increasing your heart rate
    4. Your goal is having stronger legs
    5. Your goal is having stronger ABS
    6. Your goal is having stronger shoulders and arms''')

    

choice = int(input("Choose a number between 1 to 6: "))
while choice > 6 or choice < 1:
    print("Error - It can only be a number between 1 to 6")
    print('''\nWhat do you want to get out of your training? 
    1. Your goal is losing weight
    2. Your goal is to staying calm and relax
    3. Your goal is increasing your heart rate
    4. Your goal is having stronger legs
    5. Your goal is having stronger ABS
    6. Your goal is having stronger shoulders and arms''')
    choice = int(input("Choose a number between 1 to 6: "))


training_day = int(input("\nHow many days per week you can train: "))
while training_day > 7 or training_day < 1:
    print("Error: It can only be a number between 1 to 7\n")
    training_day = int(input("How many days per week you can train: "))


print(f"\nHello {name}! Here is your training:")
print("-------------------------------------------------------------------------------------")
for count in range(1,training_day+1): # assigned one by one

    if count % 2 ==1:# it is boolean expression, check whether count is odd or even, even is 0, odd is 1

        print(f"Day {count}")
        if choice == 1:
            print("Gym workout for fat loss\n")
            print(plan_fat_loss)
            print("-------------------------------------------------------------------------------------")
        elif choice == 2:
            print("Gym workout for stretch and relax\n")
            print(plan_relax)
            print("-------------------------------------------------------------------------------------")
        elif choice == 3:
            print("Gym workout for high-intensity exercises\n")
            print(plan_high_intensity)
            print("-------------------------------------------------------------------------------------")
        elif choice == 4:
            print("Gym workout for strong legs\n")
            print(plan_legs)
            print("-------------------------------------------------------------------------------------")
        elif choice ==5:
            print("Gym workout for strong ABS\n")
            print(plan_ABS)
            print("-------------------------------------------------------------------------------------")
        elif choice == 6:
            print("Gym workout for strong shoulders and arms\n")
            print(plan_arms)
            print("-------------------------------------------------------------------------------------")
    else:
        print(f"Day {count}")
        if age < 18 and sex == "male":
            print("Gym workout for a male younger than 18 years old\n")
            print(plan_maleless18)
            print("-------------------------------------------------------------------------------------")
        elif age >= 18 and sex == "male":
            print("Gym workout for a male at least 18 years old\n")
            print(plan_maleover18)
            print("-------------------------------------------------------------------------------------")
        elif age < 18 and sex == "female":
            print("Gym workout for a female younger than 18 years old\n")
            print(plan_femaleless18)
            print("-------------------------------------------------------------------------------------")
        elif age >= 18 and sex == "female":
            print("Gym workout for a female at least 18 years old\n")
            print(plan_femaleover18)
            print("-------------------------------------------------------------------------------------")
    






print(f"\nBye {name}.")

