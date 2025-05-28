import csv
import boto3
from boto3.dynamodb.conditions import Key
from pprint import pprint


def create_table(ddb_table_name, partition_key, sort_key):
    dynamodb = boto3.resource("dynamodb")
    attribute_definitions = [
        {'AttributeName' : partition_key, 'AttributeType': 'N'},
		{'AttributeName' : sort_key, 'AttributeType': 'S'}
	]
	
    key_schema = [
	    {'AttributeName' : partition_key, 'KeyType': 'HASH'},
	    {'AttributeName' : sort_key, 'KeyType': 'RANGE'}
	    ]
	    
    provisioned_throughput = {
		'ReadCapacityUnits': 5, # low number of units to reduce costs
		'WriteCapacityUnits': 10
        }
    try:
        Table = dynamodb.create_table(
    	TableName= ddb_table_name,
    	AttributeDefinitions= attribute_definitions, 
    	KeySchema= key_schema, 
    	ProvisionedThroughput= provisioned_throughput)
    except Exception as err:
        print(f"{ddb_table_name} table could not be created.")
        
    return Table
'''
if __name__ == "__main__":
    infections = create_table("infections", "Id", "date")   


'''
def loading_table():
    with open('InfectionsData.csv') as csvfile:
        data = csv.DictReader(csvfile, delimiter = ",")
            
        dynamodb = boto3.resource("dynamodb")
        infections_table = dynamodb.Table("infections")
        for entry in data:
            sample_id = int(entry["PatientId"])
            city = entry["City"]
            date = entry["Date"]
            print(sample_id, city, date)
            infections_table.put_item(Item = {"Id" : sample_id, "city": city, "date" : date})
'''
if __name__ == "__main__":
    loading_table()

'''   
def updating_table(number, date, url):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("infections")
    response = table.update_item(
        Key = {"Id" : number, "date" : date },
        UpdateExpression = "set PatientReportUrl=:r",
        ExpressionAttributeValues={
            ':r' : url
        }
        )
    ReturnValues="UPDATED_NEW"
    return response
'''
if __name__ == "__main__":
    pprint(updating_table(1, "10/2/2015", "https://us-west-2-aws-staging.s3.amazonaws.com/awsu-ilt/AWS-100-DEV/v2.2/binaries/input/lab-3-dynamoDB/PatientRecord1.txt"))
    pprint(updating_table(2, "9/21/2015",  "https://us-west-2-aws-staging.s3.amazonaws.com/awsu-ilt/AWS-100-DEV/v2.2/binaries/input/lab-3-dynamoDB/PatientRecord2.txt"))
    pprint(updating_table(3, "9/16/2015", "https://us-west-2-aws-staging.s3.amazonaws.com/awsu-ilt/AWS-100-DEV/v2.2/binaries/input/lab-3-dynamoDB/PatientRecord3.txt"))
'''

# Checking the New Attribute, 
def query(Id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("infections")
    response = table.query(
        KeyConditionExpression=Key('Id').eq(Id)
        )
    pprint(response['Items'])
    
if __name__ == "__main__":
    query(1)
    query(2)
    query(3)
    