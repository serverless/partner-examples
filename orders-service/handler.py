import boto3
import requests
import random
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('orders-table')
sns = boto3.client('sns')

def process(event, context):
    # Set a random user for this transaction
    # All of this would normally come from event data
    user = random.choice(['alice', 'bob', 'charlie', 'david', 'eric', 'fernando'])
    user_type = random.choice(['paid', 'free'])
    context.serverless_sdk.tag_event('customerId', 5, { 'newCustomer': True, 'isDemo': True})
    context.serverless_sdk.tag_event('plan', user_type, {'optional-data': 'included with the tag', 'guid': '1237r512tye7r561ft7r5ds6a'})
    context.serverless_sdk.tag_event('user', user, {'optional-data': 'included with the tag', 'guid': '1237r512tye7r561ft7r5ds6a'})
    # Randomly throw errors
    if random.choice([True, False]):
        print("This is where a line of code will break")
        ses.send_email(Email="Stuff that's not gonna send")
        raise Exception('Whoops we made an error if we even get this far')

    # Create and delete topics
    topic = sns.create_topic(Name='slspartnertopic2')['TopicArn']
    print("Topic created: " + topic)
    sns.delete_topic(TopicArn=topic)
    print("Topic deleted: " + topic)

    # HTTP request
    print("requesting nokeynoshade data")
    r = requests.get("http://www.nokeynoshade.party/api/queens/89")
    print(r.status_code)
    print("Data:")
    print(r.text)

    # Send item into DynamoDB Table
    response = table.put_item(
        Item={'email': 'anotheremail@gmail.com'}
    )
    print("Table Item Added")
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
