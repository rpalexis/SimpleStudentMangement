import json
import datetime


def handler(event, context):
    data = {
        'name':"Rulx Philome ALEXIS",
        "description": "I'm testing CI/CD"
    }
    return {{'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}}