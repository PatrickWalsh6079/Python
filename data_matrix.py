"""
Name: data_matrix.py
Author: Patrick Walsh
Date: 2/2/2021
Purpose: Program takes in a phone number and zip code, then
has user enter two sets of 3x3 matrices and asks for
calculations on the matrices.
Uses regular expressions and numpy math operations.

Comment: Run following command to generate pylintrc file in directory
where pylint command is being run:
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc
"""

import re
import numpy as np

print("**********************************************")
print("WELCOME TO THE PYTHON MATRIX DATA APPLICATION")
print("**********************************************")


def matrix_operation(matrix1, matrix2, operation):
    """
    Function matrix_operation() converts a set of two matrices
    into a single list of elements where each element
    represents the sum, difference, or product of the corresponding
    elements in the matrices. For example, if the two matrices
    as follows are added:
    matrix1: [ [1, 1, 1], [2, 2, 2], [3, 3, 3] ]
    matrix2: [ [2, 2, 2], [2, 2, 2], [2, 2, 2] ]

    The resulting list using the matrix_operation() function is:
    [3, 3, 3, 4, 4, 4, 5, 5, 5]

    If they are subtracted, the result is:
    [-1, -1, -1, 0, 0, 0, 1, 1, 1]

    If they are multiplied, the result is:
    [2, 2, 2, 4, 4, 4, 6, 6, 6]

    Takes in three arguments(matrix1, matrix2, operation).
    """
    element = 0
    list_elements = []
    func_count = 0
    func_row = 0
    for row_matrix in matrix1:
        for item in row_matrix:
            if operation == "add":  # if using addition
                element = matrix1[func_row][func_count] + matrix2[func_row][func_count]
            elif operation == "subtract":  # if using subtraction
                element = matrix1[func_row][func_count] - matrix2[func_row][func_count]
            elif operation == "multiply":  # if using multiplication
                element = matrix1[func_row][func_count] * matrix2[func_row][func_count]
            list_elements.append(element)
            func_count += 1
            if func_count == 3:
                func_row += 1
                func_count = 0
    return list_elements


def list_to_matrix(the_list):
    """
    Function list_to_matrix() converts a list into a 3x3 Matrix.
    Takes in 1 positional argument(a list of 9 items).
    """
    new_matrix = np.arange(0, 9).reshape(3, 3)  # create new_matrix structure 3x3
    func_count = 0
    func_row = 0
    for item in the_list:
        new_matrix[func_row][func_count] = int(item)
        func_count += 1
        if func_count == 3:
            func_row += 1
            func_count = 0

    return new_matrix


def row_col_mean(matrix):
    """
    Function row_col_mean() calculates the row and column
    means of a matrix.

    Takes one positional argument (3x3 matrix).
    """
    row_means = []
    col_means = []

    # calculate row means
    row_1 = matrix[0][0] + matrix[0][1] + matrix[0][2]
    row_1_mean = row_1 / 3
    row_means.append(row_1_mean)

    row_2 = matrix[1][0] + matrix[1][1] + matrix[1][2]
    row_2_mean = row_2 / 3
    row_means.append(row_2_mean)

    row_3 = matrix[2][0] + matrix[2][1] + matrix[2][2]
    row_3_mean = row_3 / 3
    row_means.append(row_3_mean)

    # calculate column means
    col_1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
    col_1_mean = col_1 / 3
    col_means.append(col_1_mean)

    col_2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
    col_2_mean = col_2 / 3
    col_means.append(col_2_mean)

    col_3 = matrix[0][2] + matrix[1][2] + matrix[2][2]
    col_3_mean = col_3 / 3
    col_means.append(col_3_mean)

    return row_means, col_means


running = True
while running:

    # ask if user wants to play
    print("\nDo you want to play the Matrix Game?\nEnter 'y' or 'n'")
    ask_play = input(">>> ")

    if ask_play == "y":
        while True:
            # ask for phone number
            print("Enter phone number (XXX-XXX-XXXX)")
            phone_num = input(">>> ")
            # first check length
            if len(phone_num) != 12:
                print("\nInvalid phone number!")
                continue
            # then check format
            phone_num = re.search("[0-9]{3}-[0-9]{3}-[0-9]{4}", phone_num)
            if phone_num is None:
                print("\nInvalid phone number!")
                continue
            break

        while True:
            # now ask for zip code
            print("Now enter Zip Code +4 (XXXXX-XXXX)")
            zip_code = input(">>> ")
            # first check length
            if len(zip_code) != 10:
                print("\nInvalid zip code!")
                continue
            # then check format
            zip_code = re.search("[0-9]{5}-[0-9]{4}", zip_code)
            if zip_code is None:
                print("\nInvalid zip code!")
                continue
            break

        while True:
            # first 3x3 matrix
            try:
                print("\nNow enter a 3x3 Matrix (i.e., 1 2 3 4 5 6 7 8 9)")
                print("(Put a space in between each number)")
                first_3x3 = input(">>> ")
                # check length
                first_3x3 = first_3x3.split(" ")  # split user input into list
                if len(first_3x3) != 9:
                    print("\nInvalid entry!")
                    continue

                matrix_1 = np.arange(0, 9).reshape(3, 3)  # create matrix 1 structure 3x3
                # Insert user input into matrix 1
                count = 0
                row = 0
                for i in first_3x3:
                    i.strip(" ")
                    matrix_1[row][count] = int(i)
                    count += 1
                    if count == 3:
                        row += 1
                        count = 0
                # print(matrix_1)
                break
            except ValueError as err:
                print("\nPlease enter whole numbers!")
                print("Error code: ", err)

        while True:
            # second 3x3 matrix
            try:
                print("\nNow enter your second 3x3 Matrix (i.e., 1 2 3 4 5 6 7 8 9)")
                print("(Put a space in between each number)")
                second_3x3 = input(">>> ")
                # check length
                second_3x3 = second_3x3.split(" ")  # split user input into list
                if len(second_3x3) != 9:
                    print("\nInvalid entry!")
                    continue

                matrix_2 = np.arange(0, 9).reshape(3, 3)  # create matrix 2 structure 3x3
                # Insert user input into matrix 2
                count = 0
                row = 0
                for i in second_3x3:
                    i.strip(" ")
                    matrix_2[row][count] = int(i)
                    count += 1
                    if count == 3:
                        row += 1
                        count = 0
                # print(matrix_2)
                break
            except ValueError as err:
                print("\nPlease enter whole numbers!")
                print("Error code: ", err)

        while True:
            # Matrix operations
            print("Choose from the following Matrix operations:\n\na. Addition\nb. Subtraction\n"
                  "c. Matrix multiplication\nd. Element by element multiplication\n")
            matrix_choice = input(">>> ")

            if matrix_choice == "a":
                result = list_to_matrix(matrix_operation(matrix_1, matrix_2, "add"))
                print("Addition:")
            elif matrix_choice == "b":
                result = list_to_matrix(matrix_operation(matrix_1, matrix_2, "subtract"))
                print("Subtraction:")
            elif matrix_choice == "c":
                result = np.matmul(matrix_1, matrix_2)
                print("Matrix multiplication:")
            elif matrix_choice == "d":
                result = list_to_matrix(matrix_operation(matrix_1, matrix_2, "multiply"))
                print("Element by element multiplication:")
            else:
                print("\nInvalid entry!")
                continue
            print(result)
            # transpose matrix
            print("\nTranspose:")
            print(np.transpose(result))

            # row and column mean values
            print("\nRow and column means:")
            print("Row: " + "%.2f" % row_col_mean(result)[0][0],
                  "%.2f" % row_col_mean(result)[0][1],
                  "%.2f" % row_col_mean(result)[0][2])
            print("Column: " + "%.2f" % row_col_mean(result)[1][0],
                  "%.2f" % row_col_mean(result)[1][1],
                  "%.2f" % row_col_mean(result)[1][2])
            break

    # If user enters no
    elif ask_play == "n":
        print("\nTHANK YOU FOR VISITING THE PYTHON MATRIX DATA APPLICATION!!!")
        running = False
    else:
        print("\nInvalid selection!")
