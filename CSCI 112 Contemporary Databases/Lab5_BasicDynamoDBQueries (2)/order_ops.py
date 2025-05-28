#!/usr/bin/env python3
import boto3
from boto3.dynamodb.conditions import Key
import hashlib
import random
from decimal import Decimal


def add_item(order_id, product_name, quantity, price): 
    # Generate item ID. In real life, there are better
    # ways of doing this
    item_id = hashlib.sha256(product_name.encode()).hexdigest()[:8]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users-orders-items')
    
    item = {
        'pk'           : '#ITEM#{0}'.format(item_id), 
        'sk'           : '#ORDER#{0}'.format(order_id),
        'product_name' : product_name,
        'quantity'     : quantity,
        'price'        : price,
    }
    
    table.put_item(Item=item)
    print("Added {0} to order {1}".format(product_name, order_id))
    
def checkout(username, address, items, status, date): 
    # Generate order ID. In real life, there are better
    # ways of doing this
    order_id = hashlib.sha256(str(random.random()).encode()).hexdigest()[:random.randrange(1, 20)]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users-orders-items')
    
    item = {
        'pk'      : '#USER#{0}'.format(username), 
        'sk'      : '#ORDER#{0}#{1}'.format(status, order_id),
        'address' : address,
        'date' : date,
        'order_status' : status
    }
    table.put_item(Item=item)
    
    for item in items:
        add_item(order_id, 
                 item['product_name'], 
                 item['quantity'], 
                 item['price'],
                 )

def query_user_orders(username):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('users-orders-items')
    response = table.query(
        KeyConditionExpression=Key('pk').eq('#USER#{0}'.format(username)) & 
                               Key('sk').begins_with('#ORDER#')
    )
    return response['Items']
    
def query_order_items(order_id):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('users-orders-items')
    response = table.query(
        IndexName='inverted-index',
        KeyConditionExpression=Key('sk').eq('#ORDER#{0}'.format(order_id)) & 
                               Key('pk').begins_with('#ITEM#')
    )
    return response['Items']

def query_user_orders_date(username, date):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users-orders-items')
    response = table.query(
        IndexName = "date_index",
        KeyConditionExpression = Key('pk').eq('#USER#{}'.format(username)) &
                                 Key('date').eq(date)
        )
    return response['Items']
    
def query_user_orders_status(username, status):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users-orders-items')
    response = table.query(
        KeyConditionExpression = Key('pk').eq('#USER#{0}'.format(username)) &
                                 Key('sk').begins_with('#ORDER#{0}'.format(status))
        )
    return response['Items']

def query_all_pending_orders():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users-orders-items')
    response = table.query(
        IndexName = "status_pk",
        KeyConditionExpression = Key('order_status').eq('Pending') &
                                 Key('sk').begins_with('#ORDER#')
        
        )
    return response['Items']