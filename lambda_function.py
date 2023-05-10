# Time = *, Name = **

# ESSENTIAL (resources)
import json
import boto3
# import two packages to help us with dates and date formatting *
from time import gmtime, strftime

# ESSENTIAL (Link to database)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('helloWorldVisitorCounter')
# store the current time in a human readable format in a variable *
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# ESSENTIAL (link to serverless machine)
def lambda_handler(event, context):
# extract values from the event object we got from the Lambda service and store in a variable **
    name = event['firstName'] +' '+ event['lastName']

# write name and time to the DynamoDB table using the object we instantiated and save response in a variable * **
    response = table.put_item(
        Item={
            'ID': name,
            'LatestGreetingTime':now
            })
    
# return a properly formatted JSON object (Output)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda, ' + name)
    }