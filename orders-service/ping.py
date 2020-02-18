import boto3
import requests
import random
import json

def ping(event, context):
    print("requesting API data")
    r = requests.get("http://www.nokeynoshade.party/api/queens/89")
    # r = requests.get("http://www.nokeynoshade.party/api/queens/12")
    print(r.text)