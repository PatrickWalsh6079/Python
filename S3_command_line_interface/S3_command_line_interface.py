"""
Filename: S3_command_line_interface.py
Author: Patrick Walsh
Date: 6/25/2021
Purpose: Program uses boto3 to interact with S3 environment,
providing a command-line drive menu to do the following tasks:

a. Creates a S3 bucket with the name consisting of your firstname, lastname and a random 6-digit suffix. 
    For example, the following would be a possible bucket name jimrobertson-321921.
b. Puts objects in a previously created bucket.
c. Deletes an object in a bucket.
d. Deletes a bucket.
e. Copies an object from one bucket to another.
f. Downloads an existing object from a bucket.
g. Exit the program. Upon exit, the application should list the date and time.
"""

import datetime
import bucket_creater
import object_putter
import object_deleter
import bucket_deleter
import object_copier
import object_downloader
import random

# generate random suffix of 6 numbers
rando_nums = ''
for i in range(6):
    rando_nums += str(random.randint(0, 9))
    
# add random suffix to bucket name
bucket_name = 'patrickwalsh-' + rando_nums
# bucket_name = 'patrickwalsh-429101'

def main():
    print('******** WELCOME TO THE S3 COMMAND-LINE INTERFACE ********')
    while True:
        print('\nPlease choose from the following options:')
        print('a. Create S3 bucket consisting of your firstname, lastname and a random 6-digit suffix.')
        print('b. Puts objects in a previously created bucket.')
        print('c. Deletes an object in a bucket.')
        print('d. Deletes a bucket.')
        print('e. Copies an object from one bucket to another.')
        print('f. Downloads an existing object from a bucket.')
        print('g. Exit the program. Upon exit, the application should list the date and time.')
        choice = input('>>> ')
        
        if choice == 'a':
            bucket_creater.create_bucket(bucket_name)
        elif choice == 'b':
            object_putter.put_object(bucket_name, 'test_file1.txt', './week_2/test_file1.txt')
        elif choice == 'c':
            object_deleter.delete_object(bucket_name, 'test_file1.txt')
        elif choice == 'd':
            bucket_deleter.delete_bucket(bucket_name)
        elif choice == 'e':
            object_copier.copy_object('bucket1-week2', 'object_for_copy.txt', 'bucket2-week2')
        elif choice == 'f':
            object_downloader.download_object('bucket1-week2', 'object_for_copy.txt')
        elif choice == 'g':
            now = datetime.datetime.now()
            print("\nCurrent date and time: ")
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('\n\n\n******** THANK YOU FOR USING THE S3 COMMAND-LINE INTERFACE ********')
            break
        else:
            print('\n\n\nInvalid response!')
            

if __name__ == '__main__':
    main()
