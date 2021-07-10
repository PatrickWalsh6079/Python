"""
Filename: dynamo_db_interface.py
Author: Patrick Walsh
Date: 7/10/2021
Purpose: Main program that produces a CLI-style screen for the user
to interact with an AWS DynamoDB database. Lets the user initialize
the database, print records in the database, and search the database.
"""


import logging
import time
from botocore.exceptions import ClientError
import dynamo_initialize_table
import dynamo_show_records
import dynamo_search_database


def main():
    """
    Main method, generates interface for user to interact
    with database. Calls functions from other files.
    """

    print('******************************************************************')
    print('*** WELCOME TO THE PYTHON-BASED DYNAMO DATABASE INTERFACE TOOL ***')
    print('******************************************************************')

    # set to True for program to run
    program_running = True

    while program_running:

        print('Please make a selection:\n')
        print('\tA. Initialize Dynamo database')
        print('\tB. Show all database records')
        print('\tC. Search database')
        print('\tQ. Exit program')
        selection = input('>>> ')

        if selection == 'a'.lower():
            print('Initializing database...')
            dynamo_initialize_table.initialize()
            count = 0
            # wait until db is created before adding records
            while dynamo_initialize_table.status() != 'ACTIVE':
                time.sleep(0.5)
                count += 1
                if count > 40:  # times out after 20 seconds
                    print('Operation timed out....')
                    print('database initialization taking longer than expected.')
            print('Adding records...')
            dynamo_initialize_table.add_items()
            print('Database initialized!\n')

        elif selection == 'b'.lower():
            try:
                data = dynamo_show_records.show_all()  # imported from dynamo_show_records.py

                if data is not False:  # check to make sure records exist
                    print('Showing all records for Courses table:\n')
                    print('|==========|=========|============|========================================|==========|')
                    print('|CourseID  |Subject  |CatalogNbr  |Title                                   |NumCredits|')
                    print('|==========|=========|============|========================================|==========|')
                    for record in data:
                        # setup variables to create empty space after title text
                        empty_space = ' '
                        numbers = 40 - len(record["Title"])

                        print('|{}       |{}     |{}         |{}{}|{}         |'.format(
                            str(record["CourseID"]),
                            str(record["Subject"]),
                            str(record["CatalogNbr"]),
                            str(record["Title"]),
                            # insert empty space according to length of title
                            empty_space * numbers,
                            str(record["NumCredits"])))
                    print('|==========|=========|============|========================================|==========|')
                else:
                    print('Database not found. Please initialize the database!\n')
            except ClientError as err:
                logging.error(err)
                return False

        elif selection == 'c'.lower():

            # look up record by Subject and CatalogNbr
            searching = True
            while searching:
                print('Enter search criteria...\n')

                # subject = 'SDEV'
                # cat_num = 400
                while True:
                    print('Please enter a Subject (i.e. SDEV)')
                    subject = input('>>> ')
                    if subject == '':
                        print('Subject is required.')
                        continue
                    break
                while True:
                    print('Now enter a CatalogNbr (i.e. 400)')
                    cat_num = input('>>> ')
                    if cat_num == '':
                        print('CatalogNbr is required.')
                        continue
                    break

                try:

                    data = dynamo_search_database.search(subject.upper(), cat_num)
                    # print(data)
                    if data is not False:
                    # if len(data) != 0:  # if subject matches subject in database

                        match = False
                        for record in data:
                            # check if subject and cat_num match in database
                            if record['CatalogNbr'] == int(cat_num):
                                match = True
                                print('|==========|=========|============|========================================|==========|')
                                print('|CourseID  |Subject  |CatalogNbr  |Title                                   |NumCredits|')
                                print('|==========|=========|============|========================================|==========|')
                                empty_space = ' '
                                numbers = 40 - len(record["Title"])

                                print('|{}       |{}     |{}         |{}{}|{}         |'.format(
                                    str(record["CourseID"]),
                                    str(record["Subject"]),
                                    str(record["CatalogNbr"]),
                                    str(record["Title"]),
                                    # insert empty space according to length of title
                                    empty_space * numbers,
                                    str(record["NumCredits"])))
                                break
                        if not match:
                            print('\nCourse not found!')
                    else:
                        print('Database not found. Please initialize the database!\n')
                        searching = False

                    while searching:
                        print('Would you like to search for another record?')
                        search_again = input('>>> ')
                        if search_again == 'y'.lower():
                            break
                        elif search_again == 'n'.lower():
                            searching = False
                            break
                        else:
                            print('\nInvalid response!')

                except ClientError as err:
                    logging.error(err)
                    return False


        elif selection == 'q'.lower():
            print('Exiting program....\n')
            print('*** THANK YOU FOR USING THE PYTHON-BASED DYNAMO DATABASE INTERFACE TOOL ***')
            print('***************************************************************************')
            program_running = False

        else:
            print('Invalid response!\n')

if __name__ == '__main__':
    main()
