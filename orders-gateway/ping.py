import boto3
import requests
import random
import json


def ping(event, context):
    print("requesting API data")
    mock_data = {"data": "stuff"}
    submit_result = requests.post(
        "https://kuckp899sg.execute-api.us-east-1.amazonaws.com/dev/submit",
        data=mock_data
    )
    print("submit endpoint requested")
    print(submit_result)
    process_result = requests.post(
        "https://kuckp899sg.execute-api.us-east-1.amazonaws.com/dev/process",
        data=mock_data
    )
    print("process endpoint requested")
    print(process_result)
