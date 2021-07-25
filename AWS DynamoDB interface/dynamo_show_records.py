"""
Filename: dynamo_show_records.py
Author: Patrick Walsh
Date: 7/10/2021
Purpose: Program uses function to return all
records in a DynamoDB database.
"""


import logging
import boto3
from botocore.exceptions import ClientError



def show_all():
    """
    Function returns all records in database.
    """
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Courses')

        response = table.scan()

        data = []
        data = response['Items']
        # print(data)

    except ClientError as err:
        logging.error(err)
        return False
    return data
