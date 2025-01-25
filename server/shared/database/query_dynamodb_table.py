import boto3
import json
from decimal import Decimal

# DynamoDB configuration
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
TABLE_NAME = "AdvisorClientTable"

def query_clients_by_advisor(advisor_id):
    try:
        table = dynamodb.Table(TABLE_NAME)

        # Scan the table for items with the matching advisor_id
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

if __name__ == "__main__":
    # Specify the advisor ID to query
    advisor_id = 12345  # Replace with your desired advisor ID

    # Query the data
    result = query_clients_by_advisor(advisor_id)

    # Print the result in JSON format
    print(json.dumps(result, indent=4))
