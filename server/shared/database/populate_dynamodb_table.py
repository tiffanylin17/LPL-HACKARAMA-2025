import boto3
import pandas as pd

# DynamoDB configuration
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
TABLE_NAME = "AdvisorClientTable"

def populate_table_from_csv(csv_file_path):
    # Load the CSV file
    data = pd.read_csv(csv_file_path)
    table = dynamodb.Table(TABLE_NAME)

    # Iterate over the rows in the CSV and insert them into DynamoDB
    for index, row in data.iterrows():
        item = {
            "PK": f"CLIENT#{row['email']}",  # Use email as the unique identifier
            "first_name": row['first_name'],
            "last_name": row['last_name'],
            "age": int(row['age']),
            "location": row['location'],
            "client_tenure": float(row['client_tenure']),
            "interaction_freq": row['interaction_freq'],
            "last_interaction_date": row['last_interaction_date'],
            "portfolio_value": row['portfolio_value'].replace('$', '').replace(',', ''),
            "investment_growth": float(row['investment_growth']),
            "survey_results": float(row['survey_results']),
            "login_freq": int(row['login_freq']),
            "time_spent_on_cw": float(row['time_spent_on_cw']),
            "stay_leave": int(row['stay_leave'])
        }

        # Insert the item into DynamoDB
        try:
            table.put_item(Item=item)
            print(f"Inserted: {item['PK']}")
        except Exception as e:
            print(f"Error inserting {item['PK']}: {e}")

if __name__ == "__main__":
    # Replace with the path to your CSV file
    csv_file_path = "/mnt/data/MOCK_DATA (39) - MOCK_DATA (38).csv"
    populate_table_from_csv(csv_file_path)
