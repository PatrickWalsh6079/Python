"""
Name: data_analysis.py
Author: Patrick Walsh
Date: 2/14/2021
Purpose: Program reads data from a .csv file and lets
user choose specific columns in .csv file for data
analysis and histogram display.

Comment: Run following command to generate pylintrc file in directory
where pylint command is being run:
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc
"""


import matplotlib.pyplot as plt
import pandas as pd


PATH_POP = r"C:\Users\pwalsh\Desktop\School\UMGC\SDEV300\Week 5\PopChange.csv"  # set path to local .csv file
PATH_HOUSING = r"C:\Users\pwalsh\Desktop\School\UMGC\SDEV300\Week 5\Housing.csv"  # set path to local .csv file


print("*****************************************************")
print("WELCOME TO THE PYTHON DATA ANALYSIS PROGRAM (PYDATA)")
print("*****************************************************")

running = True
while running:

    print("\n1. Population data\n2. Housing data\n3. Exit")
    print("Which file would you like to analyze: (enter a number choice)")
    menu_select = input(">>> ")

    # population data
    if menu_select == "1":

        print("\nYou have chosen Population data!")
        while True:
            file_pop = open(PATH_POP, "r")  # set file path to PopChange.csv
            print("\nSelect a column to analyze:")
            print("a. Population April 1\nb. Population July 1\nc. Change Population\nd. Exit")
            col_select = input(">>> ")

            # Population April 1
            if col_select == "a":
                name = 'Pop Apr 1'
                df = pd.read_csv(PATH_POP, usecols=['Pop Apr 1'])
            # Population July 1
            elif col_select == "b":
                name = 'Pop Jul 1'
                df = pd.read_csv(PATH_POP, usecols=['Pop Jul 1'])
            # Change Population
            elif col_select == "c":
                name = 'Change Pop'
                df = pd.read_csv(PATH_POP, usecols=['Change Pop'])
            # Exit
            elif col_select == "d":
                break
            # Error catching
            else:
                print("\nInvalid entry!\n")
                continue

            count = df.count()[0]
            mean = df.mean()[0]
            std_dev = df.std()[0]
            min_pop = df.min()[0]
            max_pop = df.max()[0]

            print("Statistics for column " + name + ":\n")
            print("Count:", count)
            print("Mean:", round(mean, 2))
            print("Standard deviation:", round(std_dev, 2))
            print("Minimum:", min_pop)
            print("Maximum:", max_pop)

            # show histogram in bins of 20k from 10k to 100k
            plt.hist(df, bins=range(10000, 120000, 20000))

            plt.xlabel('Population')
            plt.ylabel('Bin Quantity')
            plt.title('Histogram of Column ' + name)
            plt.subplots_adjust(left=0.15)  # Tweak spacing to prevent clipping of ylabel
            plt.show()
            break

    # housing data
    elif menu_select == "2":

        print("\nYou have chosen Housing data!")
        while True:
            file_pop = open(PATH_HOUSING, "r")  # set file path to Housing.csv
            print("\nSelect a column to analyze:")
            print("a. AGE\nb. BEDRMS\nc. BUILT\nd. ROOMS\ne. UTILITY\nf. Exit")
            col_select = input(">>> ")

            # AGE
            if col_select == "a":
                name = 'AGE'
                df = pd.read_csv(PATH_HOUSING, usecols=['AGE'])
            # BEDRMS
            elif col_select == "b":
                name = 'BEDRMS'
                df = pd.read_csv(PATH_HOUSING, usecols=['BEDRMS'])
            # BUILT
            elif col_select == "c":
                name = 'BUILT'
                df = pd.read_csv(PATH_HOUSING, usecols=['BUILT'])
            # ROOMS
            elif col_select == "d":
                name = 'ROOMS'
                df = pd.read_csv(PATH_HOUSING, usecols=['ROOMS'])
            # UTILITY
            elif col_select == "e":
                name = 'UTILITY'
                df = pd.read_csv(PATH_HOUSING, usecols=['UTILITY'])
            # Exit
            elif col_select == "f":
                break
            # Error catching
            else:
                print("\nInvalid entry!\n")
                continue

            count = df.count()[0]
            mean = df.mean()[0]
            std_dev = df.std()[0]
            min_pop = df.min()[0]
            max_pop = df.max()[0]

            print("Statistics for column " + name + ":\n")
            print("Count:", count)
            print("Mean:", round(mean, 2))
            print("Standard deviation:", round(std_dev, 2))
            print("Minimum:", min_pop)
            print("Maximum:", max_pop)

            plt.hist(df)
            plt.xlabel('Column value')
            plt.ylabel('Quantity in bin')
            plt.title('Histogram of Column ' + name)
            plt.subplots_adjust(left=0.15)  # Tweak spacing to prevent clipping of ylabel
            plt.show()
            break

    # exit
    elif menu_select == "3":
        running = False
        print("*************************************************************")
        print("THANK YOU FOR USING THE PYTHON DATA ANALYSIS PROGRAM (PYDATA)")
        print("*************************************************************")
    else:
        print("\nInvalid entry!")
