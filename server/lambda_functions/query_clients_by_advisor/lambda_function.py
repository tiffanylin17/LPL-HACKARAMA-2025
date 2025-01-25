import boto3
import json
from decimal import Decimal

# DynamoDB configuration
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
TABLE_NAME = "AdvisorClientTable"

def decimal_default(obj):
    """
    Custom serializer for Decimal objects.
    Converts Decimal to float for JSON serialization.
    """
    if isinstance(obj, Decimal):
        return float(obj)  # or use int(obj) if appropriate
    raise TypeError

def query_clients_by_advisor(advisor_id):
    """
    Queries the DynamoDB table for all clients with the given advisor_id.
    """
    table = dynamodb.Table(TABLE_NAME)

    try:
        # Perform a scan with a filter expression
        response = table.scan(
            FilterExpression="advisor_id = :advisor_id",
            ExpressionAttributeValues={
                ":advisor_id": Decimal(str(advisor_id))
            }
        )

        # Extract items from the response
        items = response.get("Items", [])
        if not items:
            return {"status": "No clients found for the advisor."}

        return {"status": "Success", "clients": items}

    except Exception as e:
        return {"status": "Error", "message": str(e)}

def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    """
    try:
        # Handle preflight OPTIONS request
        if event['httpMethod'] == 'OPTIONS':
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",  # Allow all origins for development
                    "Access-Control-Allow-Methods": "GET, OPTIONS",  # Allowed HTTP methods
                    "Access-Control-Allow-Headers": "Content-Type",  # Allowed headers
                },
                "body": ""
            }

        # Extract advisor_id from the query string parameters
        advisor_id = event['queryStringParameters']['advisor_id']

        # Query the DynamoDB table
        result = query_clients_by_advisor(advisor_id)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",  # Allow all origins for development
                "Access-Control-Allow-Methods": "GET, OPTIONS",  # Allowed HTTP methods
                "Access-Control-Allow-Headers": "Content-Type",  # Allowed headers
            },
            "body": json.dumps(result, default=decimal_default)  # Use custom serializer
        }

    except KeyError as e:
        return {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": json.dumps({"error": "Missing advisor_id parameter"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": json.dumps({"error": str(e)})
        }
