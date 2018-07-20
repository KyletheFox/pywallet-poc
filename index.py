import json
import datetime
import sys
import requests
import index

def handler(event, context):
    
    token = "ae1cd45d2e5a4ee7a8cdfadebd7b8f7"
    url = "https://api.blockcypher.com/v1/eth/main"
    r = requests.get(url)
    print(context)
    print(event)
  
    return {'statusCode': 200,
            'body': json.loads(r.text),
            'headers': {'Content-Type': 'application/json'}}
