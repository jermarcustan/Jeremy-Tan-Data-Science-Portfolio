import boto3
import pandas

# Function to create DynamoDB table
def create_table(ddb_table_name, partition_key, sort_key):

    # Imports DynamoDB functions
    dynamodb = boto3.resource('dynamodb')
    
    # Defines attributes to be used as keys
    attribute_definitions = [
        {'AttributeName' : partition_key, 'AttributeType': 'N'},
        {'AttributeName' : sort_key, 'AttributeType': 'S'}
        ]   
    
    # Assigns defined attributes as keys
    key_schema = [
        {'AttributeName' : partition_key, 'KeyType': 'HASH'},
        {'AttributeName' : sort_key, 'KeyType': 'RANGE'}
        ]
    
    # Assigns compute units for executing program
    provisioned_throughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 10
        }
    
    # Creates table
    try:
        Table = dynamodb.create_table(
            TableName = ddb_table_name,
            AttributeDefinitions = attribute_definitions,
            KeySchema = key_schema,
            ProvisionedThroughput = provisioned_throughput
            )
        print("{} table created".format(ddb_table_name))
        return Table
    except Exception as err:
        print("{} table could not be created".format(ddb_table_name))

def load_database(ddb_table_name, url):
    
    dynamodb = boto3.resource('dynamodb')
    
    # Imports CSV file from URL
    database = pandas.read_csv(url)
    # Assigns DynamoDB table as variable to allow editing
    dtable = dynamodb.Table(ddb_table_name)
    
    # Iterates through CSV file to import data to table
    for k in range(len(database)):
        try:
            # Defines composition of attributes
            Patient = {
                'PatientId' : int(database.loc[k].at['PatientId']),
                'City' : database.loc[k].at['City'],
                'Date' : database.loc[k].at['Date']
            }
            dtable.put_item(Item=Patient)
        except Exception as err:
            print("Database could not be loaded, please reload program")
            return
        
    print("Database loaded into {}".format(ddb_table_name))
        
def update_table(ddb_table_name, index, date, url):
    
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(ddb_table_name)
    
    # Updates data based on Key (partition=index, sort=date)
    try:
        response = table.update_item(
            Key = {"PatientId" : index, "Date" : date},
            # Sets new attribute PatientReportUrl to the specified url
            UpdateExpression = "set PatientReportUrl=:r",
            ExpressionAttributeValues={
                ':r' : url
                }
            )
    except Exception as err:
        print("Database could not be updated, please reload program")
        return
        
    print("ID {} updated".format(index))
        
    return response
        
if __name__ == '__main__':

    InfDataTable = create_table(
        'InfectionsData',
        'PatientId',
        'Date'
        )

    load_database(
        'InfectionsData',
        'https://gist.githubusercontent.com/zzenonn/b9b98a09e74fbd89ec06fc9fead8eea9/raw/6ce0b34e6928bf8e436f59f46761776a8e70c85c/InfectionsData.csv'
        )
    
    update_table(
        'InfectionsData', 
        1, 
        "10/2/2015", 
        "https://us-west-2-aws-staging.s3.amazonaws.com/awsu-ilt/AWS-100-DEV/v2.2/binaries/input/lab-3-dynamoDB/PatientRecord1.txt"
        )
        
    update_table(
        'InfectionsData', 
        2, 
        "9/21/2015",  
        "https://us-west-2-aws-staging.s3.amazonaws.com/awsu-ilt/AWS-100-DEV/v2.2/binaries/input/lab-3-dynamoDB/PatientRecord2.txt"
        )
        
    update_table(
        'InfectionsData', 
        3, 
        "9/16/2015", 
        "https://us-west-2-aws-staging.s3.amazonaws.com/awsu-ilt/AWS-100-DEV/v2.2/binaries/input/lab-3-dynamoDB/PatientRecord3.txt"
        )
    
    
    
    
    
    
