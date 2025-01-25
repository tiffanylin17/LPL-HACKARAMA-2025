import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
TABLE_NAME = "AdvisorClientTable"


def lambda_handler(event, context):
    try:
        advisor_id = event['queryStringParameters']['advisor_id']
        table = dynamodb.Table(TABLE_NAME)

        # Query advisor metadata
        advisor_response = table.query(
            KeyConditionExpression="PK = :pk AND SK = :sk",
            ExpressionAttributeValues={
                ":pk": f"ADVISOR#{advisor_id}",
                ":sk": "METADATA"
            }
        )

        advisor_data = advisor_response.get("Items", [])
        if not advisor_data:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": "Advisor not found"})
            }

        # Query clients for the advisor
        clients_response = table.query(
            KeyConditionExpression="PK = :pk",
            ExpressionAttributeValues={
                ":pk": f"ADVISOR#{advisor_id}"
            }
        )

        clients = [item for item in clients_response.get("Items", []) if item["SK"] != "METADATA"]

        # Build the response
        response = {
            "advisor": advisor_data[0],
            "clients": clients
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
