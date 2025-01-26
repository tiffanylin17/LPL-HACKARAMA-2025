import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the CSV file
data = pd.read_csv("MOCK_DATA (38).csv")

# Preview the data
 # Summary statistics

# Encode categorical variables if needed
if 'categorical_column' in data.columns:
    label_encoder = LabelEncoder()
    data['encoded_column'] = label_encoder.fit_transform(data['categorical_column'])
else:
    print("Column 'categorical_column' not found in the dataset.")

# Ensure the features and target columns exist in the dataset
feature_columns = ['feature1', 'feature2', 'feature3']
target_column = 'target'

if all(col in data.columns for col in feature_columns) and target_column in data.columns:
    # Define features and target
    X = data[feature_columns]  # Input features
    y = data[target_column]  # Target labels

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the Decision Tree model
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save the trained model
    joblib.dump(model, "model.pkl")
    print("Model saved as 'model.pkl'.")
else:
    print("One or more feature or target columns are missing in the dataset.")
