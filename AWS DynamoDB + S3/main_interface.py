"""
Filename: main_interface.py
Author: Patrick Walsh
Date: 7/31/2021
Purpose: Program provides a command-line driven interface
that lets a user do online shopping from a selection of
items written to a DynamoDB database. When the user checks
the items out of their shopping cart, the items are
written to a file in S3.
"""

import time
import boto3
import dynamo_initialize_table
import dynamo_show_records


def main():
    """
    Main method, generates interface for user to interact
    with database. Calls functions from other files.
    """

    # initialize to True
    program_running = True

    print('Starting things up...')
    dynamo_initialize_table.initialize()
    count = 0
    # wait until db is created before adding records
    while dynamo_initialize_table.status() != 'ACTIVE':
        time.sleep(0.5)
        count += 1
        if count > 40:  # times out after 20 seconds
            print('Operation timed out....')
            print('App initialization taking longer than expected. Program forced to quit.')
            program_running = False
    print('Retrieving records...')
    dynamo_initialize_table.add_items()
    print('Launching interface!\n')

    print('******** WELCOME TO THE CLOUD9 SHOPPING APP ********')

    cart = []  # start with empty cart

    while program_running:
        print('\nPlease choose from the following options:')
        print('a. View shopping cart.')
        print('b. Search for item by ProductName.')
        print('c. Search for item by ProductID.')
        print('d. Browse by Category.')
        print('e. Empty shopping cart.')
        print('f. Exit the program.')
        choice = input('>>> ')

        # View shopping cart
        if choice == 'a':
            print('Shopping cart:\n', cart)

            if not cart:  # only ask to check out if cart has items
                continue
            while True:
                print('\nWould you like to check out? (y or n)')
                checkout = input('>>> ')

                if checkout == 'y':
                    cart_string = ''
                    count = 0
                    for item in cart:
                        if count == 3:
                            cart_string += '\n'
                            count = 0
                            continue
                        cart_string += item + ', '
                        count += 1

                    s3 = boto3.resource('s3')
                    object = s3.Object('shopping-cart-bucket', 'shopping_cart.txt')
                    object.put(Body=cart_string)
                    print('Items checked out:')
                    print(cart_string)
                elif checkout == 'n':
                    pass
                else:
                    print('Invalid entry!\n')
                    continue
                break

        # Search for item by ProductName
        elif choice == 'b':
            data = dynamo_show_records.show_all()  # get records from DynamoDB table

            search_name = input('Enter a product name: ')
            item_found = False
            for record in data:
                if search_name.lower() == record['ProductName'].lower():
                    print('Found')
                    print('|==========|====================|============|=========|')
                    print('|ProductID |ProductName         |Category    |Price    |')
                    print('|==========|====================|============|=========|')
                    name_space = ' '
                    num_name = 20 - len(record["ProductName"])
                    cat_space = ' '
                    num_cat = 12 - len(record["Category"])
                    price_space = ' '
                    num_price = 8 - len(record["Price"])
                    print('|{}     |{}{}|{}{}|{}{}|'.format(
                            str(record["ProductID"]),
                            str(record["ProductName"]),
                            # insert empty space according to length of ProductName
                            name_space * num_name,
                            str(record["Category"]),
                            # insert empty space according to length of Category
                            cat_space * num_cat,
                            "$" + str(record["Price"]),
                            # insert empty space according to length of Price
                            price_space * num_price))
                    print('|==========|====================|============|=========|')
                    item_found = True

                    # ask if user wants to add item to cart
                    while True:
                        print('\nAdd item to cart? (y or n)')
                        add_cart = input('>>> ')
                        if add_cart == 'y':
                            cart.append(record['ProductID'])
                            cart.append(record['ProductName'])
                            cart.append(record['Category'])
                            cart.append(record['Price'])
                            print('*** CART UPDATED ***\n')
                        elif add_cart == 'n':
                            pass
                        else:
                            print('Invalid entry!\n')
                            continue
                        break
            if item_found is False:
                print('Item not found!')

        # Search for item by ProductID
        elif choice == 'c':
            data = dynamo_show_records.show_all()  # get records from DynamoDB table

            search_id = input('Enter a product ID: ')
            item_found = False
            for record in data:
                if search_id == record['ProductID']:
                    print('Found')
                    print('|==========|====================|============|=========|')
                    print('|ProductID |ProductName         |Category    |Price    |')
                    print('|==========|====================|============|=========|')
                    name_space = ' '
                    num_name = 20 - len(record["ProductName"])
                    cat_space = ' '
                    num_cat = 12 - len(record["Category"])
                    price_space = ' '
                    num_price = 8 - len(record["Price"])
                    print('|{}     |{}{}|{}{}|{}{}|'.format(
                            str(record["ProductID"]),
                            str(record["ProductName"]),
                            # insert empty space according to length of ProductName
                            name_space * num_name,
                            str(record["Category"]),
                            # insert empty space according to length of Category
                            cat_space * num_cat,
                            "$" + str(record["Price"]),
                            # insert empty space according to length of Price
                            price_space * num_price))
                    print('|==========|====================|============|=========|')
                    item_found = True

                    # ask if user wants to add item to cart
                    while True:
                        print('\nAdd item to cart? (y or n)')
                        add_cart = input('>>> ')
                        if add_cart == 'y':
                            cart.append(record['ProductID'])
                            cart.append(record['ProductName'])
                            cart.append(record['Category'])
                            cart.append(record['Price'])
                            print('*** CART UPDATED ***\n')
                        elif add_cart == 'n':
                            pass
                        else:
                            print('Invalid entry!\n')
                            continue
                        break
            if item_found is False:
                print('Item not found!')

        # Browse by Category
        elif choice == 'd':
            categories = []
            data = dynamo_show_records.show_all()  # get records from DynamoDB table
            for record in data:
                categories.append(record['Category'])
            categories = set(categories)  # cast to set to get only unique category values
            print('Choose from one of the following categories:')
            print(categories)
            print("Type in name of category and press 'Enter'")
            cat_choice = input('>>> ')

            if cat_choice.capitalize() in categories:
                print(f'All products from {cat_choice.capitalize()} category:\n')
                print('|==========|====================|============|=========|')
                print('|ProductID |ProductName         |Category    |Price    |')
                print('|==========|====================|============|=========|')
                for record in data:
                    if cat_choice.capitalize() != record["Category"]:
                        continue
                    # setup variables to create empty space after ProductName text
                    name_space = ' '
                    num_name = 20 - len(record["ProductName"])
                    cat_space = ' '
                    num_cat = 12 - len(record["Category"])
                    price_space = ' '
                    num_price = 8 - len(record["Price"])
                    print('|{}     |{}{}|{}{}|{}{}|'.format(
                            str(record["ProductID"]),
                            str(record["ProductName"]),
                            # insert empty space according to length of ProductName
                            name_space * num_name,
                            str(record["Category"]),
                            # insert empty space according to length of Category
                            cat_space * num_cat,
                            "$" + str(record["Price"]),
                            # insert empty space according to length of Price
                            price_space * num_price))
                print('|==========|====================|============|=========|')

                # ask if user wants to add item to cart
                while True:
                    print('\nAdd item to cart? (y or n)')
                    add_cart = input('>>> ')
                    if add_cart == 'y':
                        item_choice = input('Enter ProductID: ')
                        item_found = False
                        for record in data:
                            if item_choice == record['ProductID']:
                                cart.append(record['ProductID'])
                                cart.append(record['ProductName'])
                                cart.append(record['Category'])
                                cart.append(record['Price'])
                                item_found = True
                                print('*** CART UPDATED ***\n')
                        if item_found is False:
                            print('Item not found!')
                    elif add_cart == 'n':
                        pass
                    else:
                        print('Invalid entry!\n')
                        continue
                    break
            else:
                print('Category NOT found!')

        # Empty shopping cart
        elif choice == 'e':
            print('**********************')
            print('Shopping cart emptied!')
            print('**********************')
            cart = []
            s3 = boto3.resource('s3')
            object = s3.Object('shopping-cart-bucket', 'shopping_cart.txt')
            object.put(Body='')

        # Exit the program
        elif choice == 'f':
            print('\n\n\n******** THANK YOU FOR USING THE CLOUD9 SHOPPING APP ********')
            program_running = False

        else:
            print('\n\n\nInvalid response!')

if __name__ == '__main__':
    main()
