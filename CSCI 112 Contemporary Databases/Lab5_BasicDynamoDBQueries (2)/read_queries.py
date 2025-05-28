import user_ops as user
import order_ops as order_ops   
from decimal import Decimal
import boto3
from boto3.dynamodb.conditions import Key

if __name__ == '__main__':

    print(user.query_user_profile("tgrimes1"))

    orders = order_ops.query_user_orders("tgrimes1")

    for order in orders:
        order_id = order['sk'][15:] # Remove order prefix
        items = order_ops.query_order_items(order_id)
        print(items)
        for item in items:
            print(item['product_name'])
    
    def date_query(username, date):
        print('\nFiltering based on date\n')
        order_data = order_ops.query_user_orders_date(username, date)
        print(order_data)
        for order in order_data:
            if order == []:
                continue
            order_no = order["sk"][15:]
            print(f' Order Number is {order_no}')
            items = order_ops.query_order_items(order_no)
            print("The list of items under this order are listed below:")
            for item in items:
                print(item['product_name'])
    
    def status_query(username, status):
        print('\nFiltering based on status\n')
        order_data = order_ops.query_user_orders_status(username, status)
        print(order_data)
        for order in order_data:
            if order == []:
                continue
            order_no = order["sk"][15:]
            print(f' Order Number is {order_no}')
            items = order_ops.query_order_items(order_no)
            print("The list of items under this order are listed below:")
            for item in items:
                print(item['product_name'])
                
    def all_pending():
        print('\nFinding all the Pending Orders\n')
        print(order_ops.query_all_pending_orders())
        pending_orders = order_ops.query_all_pending_orders()
        for order in pending_orders:
            order_index = order["sk"][15:]
            print(f'Pending Orders for Order Number: {order_index}')
            items = order_ops.query_order_items(order_index)
            for item in items:
                print(item['product_name'])
                
    #Testing Orders from "aarchamb" on January 10, 2021
    
    date_query("aarchamb", "2021-01-10")
    
    #Testing Orders from aarchamb which are still pending
    
    status_query("tgrimes1", "Pending")

    #Get all Pending Orders
    
    all_pending()
    
    
    