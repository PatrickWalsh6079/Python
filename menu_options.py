'''
Name: menu_options.py
Author: Patrick Walsh
Date: 1/23/2021
Purpose: Create a menu-driven Python application that gives users the option to do the following:
a. Generate secure password
b. Calculate calorie intake percentage
c. How many days from today until July 4, 2025
d. Use the Law of Cosines to calculate the side of a triangle
e. Calculate the volume of a right circular cylinder
6. Exit program

Comment: Run following command to generate pylintrc file in directory
where pylint command is being run:
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc
'''

import secrets
import random
import string
import math
from datetime import date

# variables for generating secure password
LOWERCASE_LETTERS = string.ascii_letters[:26]
UPPERCASE_LETTERS = string.ascii_letters[26:]
NUMBERS = string.digits
SPECIAL_CHARACTERS = string.punctuation

print("***********************************************************")
print("\t\t\t\t\tWELCOME TO LAB 2!\n\t\tPLEASE CHOOSE FROM THE FOLLOWING OPTIONS:")
print("***********************************************************")


# show menu options
running_program = True

while running_program:
    menu_choices = input("a. Generate secure password\n"
                         "b. Calculate calorie intake percentage\n"
                         "c. How many days from today until July 4, 2025\n"
                         "d. Use the Law of Cosines to calculate the side of a triangle\n"
                         "e. Calculate the volume of a right circular cylinder\n"
                         "f. Exit program\nENTER LETTER CHOICE: ")

    # CHOICE A
    # secure password
    if menu_choices == "a":
        print("\n" * 40)

        while True:
            try:
                print("\nSECURE PASSWORD GENERATOR:")

                length_password = int(input("\nLength of password: (enter a whole number) "))
                case_password = input("Include uppercase and lowercase? (enter 'y' or 'n') ")
                if case_password not in ('y', 'n'):
                    print("\nInvalid input!")
                    continue
                numbers_password = input("Include numbers? (enter 'y' or 'n') ")
                if numbers_password not in ('y', 'n'):
                    print("\nInvalid input!")
                    continue
                special_char_password = input("Include special characters? (enter 'y' or 'n') ")
                if special_char_password not in ('y', 'n'):
                    print("\nInvalid input!")
                    continue

                # generate secure password from secret module
                password = ""
                # iterate for the length of the password
                for i in range(length_password):
                    # get a random lowercase letter, uppercase letter, number, and special character
                    characters = [secrets.choice(LOWERCASE_LETTERS)]
                    # check if password should have something other than lowercase letters
                    if case_password == "y":
                        characters.append(secrets.choice(UPPERCASE_LETTERS))
                    if numbers_password == "y":
                        characters.append(secrets.choice(NUMBERS))
                    if special_char_password == "y":
                        characters.append(secrets.choice(SPECIAL_CHARACTERS))

                    # randomly add one of the characters to the password string
                    if len(characters) == 1:
                        password += characters[0]
                    else:
                        password += characters[random.randint(0, len(characters)-1)]
                print("Password:", password)

                # ask if user wants to make another selection from the menu
                while True:
                    another_selection = input("\n\nMake another selection? ('y' or 'n') ")
                    if another_selection == "y":
                        print("\n" * 40)
                    elif another_selection == "n":
                        running_program = False
                    else:
                        print("Invalid choice! Please enter 'y' or 'n'")
                        continue
                    break
                break
            except ValueError as err:
                print("\nInvalid input! Must enter a number.\nError message: ", err)
                continue

    # CHOICE B
    # calculate percentage
    elif menu_choices == "b":
        print("\n" * 40)

        while True:
            try:
                print("\nCALORIE INTAKE PERCENTAGE CALCULATOR:")
                denominator = float(input("\nEnter your daily calorie intake goal: "))
                numerator = float(input("Now enter the number of calories you consumed today: "))
                decimals = int(input("Enter the number of decimals: "))
                decimals = "%." + str(decimals) + "f"
                percentage = (numerator / denominator) * 100
                print("You consumed", decimals % percentage + "%", "of your daily calorie goal!")

                # ask if user wants to make another selection from the menu
                while True:
                    another_selection = input("\n\nMake another selection? ('y' or 'n') ")
                    if another_selection == "y":
                        print("\n" * 40)
                    elif another_selection == "n":
                        running_program = False
                    else:
                        print("Invalid choice! Please enter 'y' or 'n'")
                        continue
                    break
                break
            except ZeroDivisionError as err:
                print("\nInvalid input! Cannot divide by zero.\nError message: ", err)
                continue
            except ValueError as err:
                print("\nInvalid input! Must enter a number.\nError message: ", err)
                continue

    # CHOICE C
    # how many days until 4 July, 2025
    elif menu_choices == "c":
        print("\n" * 40)

        print("\nHOW MANY DAYS UNTIL JULY 4, 2025:\n")
        # use datetime module to calculate days
        today = date.today()
        # date to be checked
        date_check = date(2025, 7, 4)
        # calculate how many days until
        days_until = date_check - today
        days_until = days_until.days
        print("Today's date: ", today, "\nDays until 7/4/2025: ", days_until)

        # ask if user wants to make another selection from the menu
        while True:
            another_selection = input("\n\nMake another selection? ('y' or 'n') ")
            if another_selection == "y":
                print("\n" * 40)
            elif another_selection == "n":
                running_program = False
            else:
                print("Invalid choice! Please enter 'y' or 'n'")
                continue
            break

    # CHOICE D
    # use Law of Cosines
    elif menu_choices == "d":
        print("\n" * 40)

        while True:
            try:
                print("\nLAW OF COSINES CALCULATOR:")
                print("{Formula: c^2 = a^2 + b^2 − 2ab cos(C)}")
                print("(Assume all values are in feet)")
                a = float(input("\nTo solve for length of side c, enter the length of side a: "))
                b = float(input("Now enter the length of side b: "))
                angle_c = float(input("Finally, enter the angle of C in degrees: "))
                # Law of Cosines formula:
                answer = math.sqrt(a**2 + b**2 - (2*a*b * math.cos(math.radians(angle_c))))
                # round to 2 decimals
                answer = ("%.2f" % answer)
                print("Length of side c =", answer, "ft")

                # ask if user wants to make another selection from the menu
                while True:
                    another_selection = input("\n\nMake another selection? ('y' or 'n') ")
                    if another_selection == "y":
                        print("\n" * 40)
                    elif another_selection == "n":
                        running_program = False
                    else:
                        print("Invalid choice! Please enter 'y' or 'n'")
                        continue
                    break
                break
            except ValueError as err:
                print("\nInvalid input! Must enter a number.\nError message: ", err)
                continue

    # CHOICE E
    # calculate volume of right circular triangle
    elif menu_choices == "e":
        print("\n" * 40)

        while True:
            try:
                print("\nCALCULATE VOLUME OF RIGHT CIRCULAR CYLINDER:")
                print("{Formula: Volume = (Pi * radius^2) * height}")
                print("(Assume all values are in feet)")
                height = float(input("\nEnter the height of the right cylinder: "))
                radius = float(input("Now enter the radius of the right cylinder: "))
                volume = (math.pi * radius**2) * height
                # round to 2 decimals
                volume = ("%.2f" % volume)
                print("Volume:", volume, "sq ft")

                # ask if user wants to make another selection from the menu
                while True:
                    another_selection = input("\n\nMake another selection? ('y' or 'n') ")
                    if another_selection == "y":
                        print("\n" * 40)
                    elif another_selection == "n":
                        running_program = False
                    else:
                        print("Invalid choice! Please enter 'y' or 'n'")
                        continue
                    break
                break
            except ValueError as err:
                print("\nInvalid input! Must enter a number.\nError message: ", err)
                continue

    # CHOICE F
    # exit program
    elif menu_choices == "f":
        running_program = False
        print("THANK YOU FOR USING THE LAB 2 PYTHON APPLICATION!!!")
        break

    # invalid response
    else:
        print("\nInvalid input!\nPlease enter a letter choice from the menu:")
        continue

    # if user exits after using the program
    if not running_program:
        print("THANK YOU FOR USING THE LAB 2 PYTHON APPLICATION!!!")
