import json


def lambda_handler(event, context):
    n = int(event['n'])
    sqr = n ** 2
    return {
        'statusCode': 200,
        'body': json.dumps(sqr)
    }
