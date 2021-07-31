"""
Filename: dynamo_initialize_table.py
Author: Patrick Walsh
Date: 7/31/2021
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
            TableName='ShoppingItems',
                KeySchema=[
                    {
                    'AttributeName': 'ProductID',
                    'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                    'AttributeName': 'ProductID',
                    'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
        )
    except ClientError:
        return False
    return table


def add_items():
    """
    Function adds records to database.
    """
    try:
        table = dynamodb.Table('ShoppingItems')
        # Table attributes:
        # ProductID (String) – Serves as the Hash Key. (e.g. 43001)
        # ProductName (String) – (e.g. Toothpaste)
        # Category (String) – (e.g. Bathroom)
        # Price (Number) - (e.g. 19.99)
        items_array = [['76544','Sugar', 'Food', '8.99'],
            ['46575','Toothpaste', 'Bathroom', '5.99'],
            ['75421','Gaming headset', 'Electronics', '45.99'],
            ['02487','Potatoes', 'Food', '3.99'],
            ['12247','Sneakers, mens', 'Footwear', '79.99'],
            ['35582','Laptop', 'Electronics', '999.99'],
            ['22448','Canned soup', 'Food', '2.99'],
            ['12054','Deodorant', 'Bathroom', '6.99'],
            ['45742','Phone case', 'Electronics', '19.99'],
            ['12544','Mouthwash', 'Bathroom', '12.99'],
            ['87943','Hiking boots', 'Footwear', '179.99'],
            ['23435','Socks, white', 'Footwear', '4.99'],
            ['09856','Dog food, canned', 'Pets', '0.99'],
            ['18358','Tent', 'Camping', '149.99'],
            ['26587','T-shirt', 'Clothing', '10.0'],
            ['24576','Microphone', 'Electronics', '89.99'],
            ['24876','Toothbrush', 'Bathroom', '6.99'],
            ['98043','Frozen pizza', 'Food', '5.99'],
            ['22657','Fire starter', 'Camping', '3.99'],
            ['36578','Cat food, dry', 'Pets', '12.99'],
            ['24376','iPhone', 'Electronics', '900.0'],
            ['89065','Cat scratching post', 'Pets', '24.99'],
            ['45331','Shoes, childrens', 'Footwear', '31.99'],
            ['78997','Socks, argyle', 'Footwear', '8.99'],
            ['35709','Shorts', 'Clothing', '35.99'],
            ['15739','Underwear, mens', 'Clothing', '6.99'],
            ['25467','Socks, black', 'Footwear', '4.99'],
            ['25467','Cell phone charger', 'Electronics', '14.99'],
            ['76896','Portable stove', 'Camping', '57.98'],
            ['44565','Lantern', 'Camping', '34.99'],
            ['34657','Flip flops', 'Footwear', '25.99'],
            ['34657','Android', 'Electronics', '799.99'],
            ['98704','Gaming PC', 'Electronics', '2578.99'],
            ['23565','Scarf', 'Clothing', '10.59']]

        for item in items_array:
            pid = item[0]
            pnm = item[1]
            cat = item[2]
            prc = item[3]

            table.put_item(
                Item={
                    'ProductID': pid,
                    'ProductName': pnm,
                    'Category': cat,
                    'Price': prc
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
    table = dynamodb.Table('ShoppingItems')
    return table.table_status
