import boto3

def create_dynamodb_table():
    # Initialize DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    # Define the table schema
    table_name = "AdvisorClientTable"
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {'AttributeName': 'PK', 'KeyType': 'HASH'},  # Partition Key
                {'AttributeName': 'SK', 'KeyType': 'RANGE'}  # Sort Key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'PK', 'AttributeType': 'S'},  # String
                {'AttributeName': 'SK', 'AttributeType': 'S'}   # String
            ],
            BillingMode='PAY_PER_REQUEST',  # On-demand billing
        )

        # Wait for the table to be created
        print("Creating table...")
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        print(f"Table '{table_name}' created successfully!")

    except Exception as e:
        print(f"Error creating table: {e}")

if __name__ == "__main__":
    create_dynamodb_table()
