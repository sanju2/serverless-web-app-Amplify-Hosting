import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('simple-webapp')

def lambda_handler(event, context):
    gmt_time = time.gmtime()
    now = time.strftime('%a, %d %b %Y %H:%M:%S +0000', gmt_time)
    name = event['firstName'] +' '+ event['lastName']
    
    response = table.put_item(
        Item={
            'ID': name,
            'LatestGreetingTime':now
            })

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda, ' + name)
    }