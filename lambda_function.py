# Libraries added for AWS, json, and time
import boto3
# import json
from time import gmtime, strftime

# variable for Lambda_handler2 func, to set what time it is currently
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

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

    # global count
    count = response['Attributes']['count']

    return {
        'statusCode': 200,
        'body': 'Count: ' + str(count)
    }

# # Func for showing when the site was visited in lambda by number (toa=time of arrival), then sends a json dump back to the site
# def lambda_handler(event, context):
#     response = table.put_item(
#         Item={
#             'count': str(count),
#             'VisitedTime': now
#             }
#     )
    
#     return {
#         'statusCode': 200,
#         'body': json.dumps("Hello from Lambda, No." + str(count) + ", at " + str(now) + ".")
#     }
