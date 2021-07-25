"""
Filename: dynamo_search_database.py
Author: Patrick Walsh
Date: 7/10/2021
Purpose: Program uses functions to let user
search a DynamoDB database.
"""


import logging
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr


def search(subject, cat_num):
    """
    Function lets user search DynamoDB database.
    Takes in 2 arguments: subject, and cat_num.
    """
    try:
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table('Courses')

        # response = table.query(
        #     KeyConditionExpression=Key('CourseID').eq('001')
        # )

        response = table.scan(
            FilterExpression=Attr('Subject').eq(subject)
        )
        items = response['Items']
        # print(items)
    except ClientError as err:
        logging.error(err)
        return False
    return items
