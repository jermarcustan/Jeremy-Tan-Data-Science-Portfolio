#!/usr/bin/env python3
import boto3

def create_invertible_table(
        ddb_table_name,
        partition_key,
        sort_key,
        lsi,
        lsi_2
        ):

    dynamodb = boto3.resource('dynamodb')

    # The variables below transform the arguments into the parameters expected by dynamodb.create_table.

    table_name = ddb_table_name
    
    attribute_definitions = [
        {'AttributeName': partition_key, 'AttributeType': 'S'},
        {'AttributeName': sort_key, 'AttributeType': 'S'},
        {'AttributeName' : lsi, 'AttributeType' : 'S'},
        {'AttributeName' : lsi_2, 'AttributeType' : 'S'}
        ]
    
    key_schema = [{'AttributeName': partition_key, 'KeyType': 'HASH'}, 
                  {'AttributeName': sort_key, 'KeyType': 'RANGE'}]
                  
    provisioned_throughput = {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    
    global_secondary_indexes = [
        {
            'IndexName': 'inverted-index',
            'KeySchema': [
                {'AttributeName': sort_key, 'KeyType': 'HASH'},
                {'AttributeName': partition_key, 'KeyType': 'RANGE'}],
            'Projection': {'ProjectionType': 'INCLUDE',
                           'NonKeyAttributes': ['quantity',	'price', 'status', 'product_name']
            },
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
        },
        {
            'IndexName': 'status_pk',
            'KeySchema': [
                {'AttributeName': lsi_2, 'KeyType': 'HASH'},
                {'AttributeName': sort_key, 'KeyType': 'RANGE'}],
            'Projection': {'ProjectionType': 'INCLUDE',
                           'NonKeyAttributes': ['quantity',	'price', 'status', 'product_name']
            },
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
        }
    ]
    
    local_secondary_indexes = [
    {
        'IndexName' : 'date_index',
        'KeySchema' : [
            {'AttributeName': partition_key, 'KeyType': 'HASH'}, 
            {'AttributeName': lsi, 'KeyType': 'RANGE'}    
            ],
        'Projection' : {'ProjectionType' : 'ALL'}
    },
    {
        'IndexName' : 'status_index',
        'KeySchema' : [
            {'AttributeName': partition_key, 'KeyType': 'HASH'}, 
            {'AttributeName': lsi_2, 'KeyType': 'RANGE'}    
            ],
        'Projection' : {'ProjectionType' : 'ALL'}
    }]
    
    try:
        # Create a DynamoDB table with the parameters provided
        table = dynamodb.create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attribute_definitions,
                                      ProvisionedThroughput=provisioned_throughput,
                                      LocalSecondaryIndexes = local_secondary_indexes,
                                      GlobalSecondaryIndexes = global_secondary_indexes
                                      )
        return table
    except Exception as err:
        print("{0} Table could not be created".format(table_name))
        print("Error message {0}".format(err))
        
def delete_table(name):
    dynamodb = boto3.resource('dynamodb')  
    table = dynamodb.Table(name)
    table.delete()

if __name__ == '__main__':
    table = create_invertible_table("users-orders-items", "pk", "sk", "date", "order_status")
    
    # delete_table("users-orders-items")
