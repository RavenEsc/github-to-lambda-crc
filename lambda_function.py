import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('helloWorldVisitorCounter')

def lambda_handler(event, context):
    response = table.update_item(
        Key={
            'key': 'visitor-counter'
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

    count = response['Attributes']['count']
    return {
        'statusCode': 200,
        'body': 'Count: ' + str(count)
    }

# # Time = *, Name = **

# # ESSENTIAL (resources)
# import json
# import boto3
# # import two packages to help us with dates and date formatting *
# from time import gmtime, strftime

# # ESSENTIAL (Link to database)
# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('helloWorldVisitorCounter')
# # store the current time in a human readable format in a variable *
# now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# # ESSENTIAL (link to serverless machine)
# def lambda_handler(event, context):
# # extract values from the event object we got from the Lambda service and store in a variable **
#     name = event['firstName'] +' '+ event['lastName']

# # write name and time to the DynamoDB table using the object we instantiated and save response in a variable * **
#     response = table.put_item(
#         Item={
#             'ID': name,
#             'LatestGreetingTime':now
#             })
    
# # return a properly formatted JSON object (Output)
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda, ' + name)
#     }


# import boto3
# import json
# from time import gmtime, strftime, time

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('helloWorldVisitorCounter')

# now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# # starts at 0
# counter = 0
# # infinite counter, delays a second, ends when it reaches 3
# if :
#     counter += 1
#     print(counter)
#     time.sleep(1)
#     if counter >= 3:
#         break

# def lambda_handler(context):
#     response = table.put_item(
#         Item={
#             'VisitCount': counter
#             'LatestGreetingTime': now
#             }
#     )
    
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda, NO.' + counter)
#     }