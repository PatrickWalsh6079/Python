"""
Filename: dynamo_initialize_table.py
Author: Patrick Walsh
Date: 7/10/2021
Purpose: Program uses functions to create a DynamoDB
database, enter records into the database, and
check the status of the database.
"""


import logging
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')


def initialize():
    """
    Function initializes database.
    """
    try:
        table = dynamodb.create_table(
            TableName='Courses',
                KeySchema=[
                    {
                    'AttributeName': 'CourseID',
                    'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                    'AttributeName': 'CourseID',
                    'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
        )
    except ClientError as err:
        logging.error(err)
        return False
    return table


def add_items():
    """
    Function adds records to database.
    """
    try:
        table = dynamodb.Table('Courses')
        # Table attributes:
        # CourseID (String) – Serves as the Hash Key. (e.g. 001)
        # Subject (String) – (e.g. SDEV)
        # CatalogNbr (Number) – (e.g. 400)
        # Title (String) – (e.g. Secure Programming in the Cloud)
        # NumCredits (Number) - (e.g. 3)
        courses_array = [['001','SDEV', 400, "Secure Programming in the Cloud", 3],
            ['002','CMSC', 307, "Artificial Intelligence App", 3],
            ['003','CMSC', 325, "Game Design and Development", 3],
            ['004','CMSC', 495, "Trends Projects Comp Science", 3],
            ['005','SDEV', 460, "Software Security Testing", 3],
            ['006','CMSC', 427, "Artificial Intell Foundations", 3],
            ['007','SDEV', 425, "Mitigating Software Vulnerabilities", 3],
            ['008','CMIS', 320, "Relatnl Dtbs Concepts & Apps", 3],
            ['009','SDEV', 325, "Detecting SW Vulnerabilities", 3],
            ['010','SDEV', 350, "Database Security", 3]]

        for item in courses_array:
            cid = item[0]
            sbj = item[1]
            cnum = item[2]
            title = item[3]
            numc = item[4]

            table.put_item(
                Item={
                    'CourseID': cid,
                    'Subject': sbj,
                    'CatalogNbr': cnum,
                    'Title': title,
                    'NumCredits': numc
                }
        )
    except ClientError as err:
        logging.error(err)
        return False
    return True


def status():
    """
    Function checks status of database to see if it exists.
    """
    table = dynamodb.Table('Courses')
    return table.table_status
