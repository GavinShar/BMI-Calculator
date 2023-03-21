user_ft = 0
user_in = 0
user_lbs = 0
user_kg = 0
user_m = 0
user_bmi = 0
collected_info_bool = False
#tells user what info will be asked of them
print("Welcome to Gavin's BMI Calculator.\nPlease enter your height in feet then inches when prompted.")
#gets feet of height from user
while not collected_info_bool:
    try:
        user_ft = int(input("Feet: "))
        if user_ft > 8 or 1 > user_ft:
            print("Value entered must be a integer between 1 and 8. Please try again.")
            continue
        else:
            collected_info_bool = True
    except ValueError:
        print("Value entered must be a integer between 1 and 8. Please try again.")
        continue

collected_info_bool = False
#gets inches of height from user
while not collected_info_bool:
    try:
        user_in = int(input("Inches: "))
        if user_in > 11 or user_in < 1:
            print("Value entered must be a integer between 1 and 11. Please try again.")
            continue
        else:
            collected_info_bool = True
    except ValueError:
        print("Value entered must be a integer between 1 and 11. Please try again.")
        continue
#converts feet + inches to just inches
user_in = user_in + (user_ft * 12)
#converts inches to meters
user_m = user_in * 0.025
#print("The user in meters is: ", user_m)

collected_info_bool = False
#gets weight in lbs from user
while not collected_info_bool:
    try:
        user_lbs = float(input("Please enter in your weight in lbs: "))
        if user_lbs > 1400 or user_lbs < 5:
            print("Value entered is not in range, please try again.")
            continue
        else:
            collected_info_bool = True
    except ValueError:
        print("Value entered is not a number, please try again.")
        continue
#converts weight in lbs to kg
user_kg = user_lbs * 0.45
#calculates user's bmi
user_bmi = user_kg / (user_m ** 2)

print("Your bmi is: ", user_bmi)
#tells user which bmi class they fall into
if user_bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= user_bmi < 25:
    print("You are a normal weight.")
elif 25 <= user_bmi < 30:
    print("You are overweight.")
elif user_bmi >= 30:
    print("You are Obese.")