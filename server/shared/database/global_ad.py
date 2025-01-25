import boto3
def global_ad():
    print("test")
    dynamodb = boto3.client('dynamodb', region_name='us-west-2')

    response = dynamodb.update_table(
        TableName="AdvisorClientTable",
        AttributeDefinitions=[
            {"AttributeName": "advisor_id", "AttributeType": "N"}
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": "AdvisorIndex",
                    "KeySchema": [
                        {"AttributeName": "advisor_id", "KeyType": "HASH"}
                    ],
                    "Projection": {"ProjectionType": "ALL"},
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 5,
                        "WriteCapacityUnits": 5
                    }
                }
            }
        ]
    )
    print("GSI added successfully:", response)

if __name__ == "__main__":
    global_ad()