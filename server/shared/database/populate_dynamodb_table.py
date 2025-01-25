import boto3
import pandas as pd
from decimal import Decimal

# DynamoDB configuration
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
TABLE_NAME = "AdvisorClientTable"

def populate_table_from_csv(csv_file_path):
    # Load the CSV file
    data = pd.read_csv(csv_file_path)
    table = dynamodb.Table(TABLE_NAME)

    # Iterate over the rows in the CSV and insert them into DynamoDB
    for index, row in data.iterrows():
        # Convert row to a dictionary and ensure float values are converted to Decimal
        item = {
            "PK": f"CLIENT#{row['email']}",  # Use email as the unique identifier
            "first_name": row['first_name'],
            "last_name": row['last_name'],
            "age": int(row['age']),
            "location": row['location'],
            "client_tenure": Decimal(str(row['client_tenure'])),
            "interaction_freq": row['interaction_freq'],
            "last_interaction_date": row['last_interaction_date'],
            "portfolio_value": Decimal(str(row['portfolio_value'].replace('$', '').replace(',', ''))),
            "investment_growth": Decimal(str(row['investment_growth'])),
            "survey_results": Decimal(str(row['survey_results'])),
            "login_freq": int(row['login_freq']),
            "time_spent_on_cw": Decimal(str(row['time_spent_on_cw'])),
            "stay_leave": int(row['stay_leave']),
            "advisor_id": int(row['advisor_id'])
        }

        # Insert the item into DynamoDB
        try:
            table.put_item(Item=item)
            print(f"Inserted: {item['PK']}")
        except Exception as e:
            print(f"Error inserting {item['PK']}: {e}")

if __name__ == "__main__":
    # Replace with the path to your CSV file
    csv_file_path = "/Users/ryanbouzan/PycharmProjects/LPL-HACKARAMA-2025/server/shared/database/MOCK_DATA (39).csv"
    populate_table_from_csv(csv_file_path)
