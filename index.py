import json
import datetime
import sys
import requests

def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    
    token = "ae1cd45d2e5a4ee7a8cdfadebd7b8f7"
    url = "https://api.blockcypher.com/v1/eth/main"
    r = requests.get(url)
    print(r.text)
  
    return {'statusCode': 200,
            'body': json.dumps(r),
            'headers': {'Content-Type': 'application/json'}}
