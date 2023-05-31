# Libraries added for AWS, json, and time
import boto3
import json
# from time import gmtime, strftime

# variable for Lambda_handler2 func, to set what time it is currently
# now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# variables for attaching the dynamodb table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('helloWorldVisitorCounter')

# Func for counting the amount of times this code is executed in lambda (oc=overall count)
def lambda_handler(event, context):
    response = table.update_item(
        Key={
            'ID': 'visit-count'
        },
        UpdateExpression='ADD #c :increment',
        ExpressionAttributeNames={
            "#c": "count"
        },
        ExpressionAttributeValues={
            ':increment': 1
        },
        ReturnValues='UPDATED_NEW'
    )

    # global counter
    counter = response['Attributes']['count']
    json_data = {'counter': int(counter)}
    
    print(counter)
    return {
        "statusCode": 200,
        "body": json.dumps(json_data),
    "headers": {
            "Access-Control-Allow-Origin": "https://www.ravens-resume-crc.com",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
            "Content-Type": "application/json"
        }
    }