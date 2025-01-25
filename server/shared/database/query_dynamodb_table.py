import boto3

def query_dynamodb_table(advisor_id):
    # Initialize DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table_name = "AdvisorClientTable"
    table = dynamodb.Table(table_name)

    # Query advisor metadata
    response = table.query(
        KeyConditionExpression="PK = :pk AND SK = :sk",
        ExpressionAttributeValues={
            ":pk": f"ADVISOR#{advisor_id}",
            ":sk": "METADATA"
        }
    )
    print("Advisor Metadata:", response.get("Items", []))

    # Query all clients for the advisor
    response = table.query(
        KeyConditionExpression="PK = :pk",
        ExpressionAttributeValues={
            ":pk": f"ADVISOR#{advisor_id}"
        }
    )
    print("Clients:", [item for item in response.get("Items", []) if item["SK"] != "METADATA"])

if __name__ == "__main__":
    advisor_id = "123"  # Replace with the advisor ID you want to query
    query_dynamodb_table(advisor_id)
