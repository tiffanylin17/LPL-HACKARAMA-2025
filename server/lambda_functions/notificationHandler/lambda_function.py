import json

def lambda_handler(event, context):
    """
    Test Lambda function that responds with 'Hello'.
    """
    query_params = event.get('queryStringParameters', {})

    name = query_params.get('name')
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"  # Enable CORS if needed
        },
        "body": json.dumps({
            "name": name
        })
    }
