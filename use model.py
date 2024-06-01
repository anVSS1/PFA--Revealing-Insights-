import pandas as pd
from datetime import datetime
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = joblib.load('churn_prediction_model.pkl')  # Ensure correct model file path

# Load new customer data 
new_data = pd.read_csv('new_customer_data.csv')  # Replace with the actual file path

# Preprocess the new data 
def preprocess_new_data(new_df):
    new_df['Date Commande'] = pd.to_datetime(new_df['Date Commande'], format="%Y-%m-%d")  # Make sure the date format matches
    client_features_new = new_df.groupby('ID Client').agg({
        'ID Commande': 'nunique', 
        'Total': ['mean', 'max', 'min', 'std'],
        'ID Article': 'nunique',
        'Date Commande': ['min', 'max']  
    }).reset_index()

    # Flatten and rename columns
    client_features_new.columns = [' '.join(col).strip() for col in client_features_new.columns.values]
    client_features_new.rename(columns={
        'ID Client ': 'ID Client',
        'ID Commande nunique': 'Total Orders',
        'Total mean': 'Average Order Value',
        'Total max': 'Max Purchase Value',
        'Total min': 'Min Purchase Value',
        'Total std': 'Std Dev Order Value',
        'ID Article nunique': 'Unique Products Purchased',
        'Date Commande min': 'First Purchase Date',
        'Date Commande max': 'Last Purchase Date'
    }, inplace=True)

    # Calculate additional features (same calculations as in training)
    current_date = pd.to_datetime('today')
    client_features_new['Time Since First Purchase'] = (current_date - client_features_new['First Purchase Date']).dt.days
    client_features_new['Time Since Last Purchase'] = (current_date - client_features_new['Last Purchase Date']).dt.days
    client_features_new['Purchase Frequency'] = client_features_new['Total Orders'] / client_features_new['Time Since First Purchase']
    client_features_new.replace([np.inf, -np.inf], np.nan, inplace=True)
    client_features_new.fillna(0, inplace=True) # Replace inf and NaN with 0
    client_features_new['Change in Purchase Frequency'] = client_features_new.apply(calculate_frequency_change, axis=1)

    # Drop columns (same as in training)
    new_data = client_features_new.drop(['ID Client', 'First Purchase Date', 'Last Purchase Date'], axis=1)

    # Ensure columns are in the same order as the training data
    new_data = new_data[X_train.columns]

    return new_data


# Apply the same transformations to new_data
prepared_new_data = preprocess_new_data(new_df)

# Standardize the new data using the saved scaler from the training (make sure to load the scaler object)
prepared_new_data_scaled = scaler.transform(prepared_new_data)


# Make predictions on the new data
predictions = loaded_model.predict(prepared_new_data_scaled)
probabilities = loaded_model.predict_proba(prepared_new_data_scaled)[:, 1]

# Create DataFrame with predictions and probabilities
results = pd.DataFrame({
    'ID Client': client_features_new['ID Client'],  # Assuming you have 'ID Client' in the new data
    'Predicted Churn': predictions,
    'Churn Probability': probabilities
})

print(results)

Total of Quantities = SUM(data_cleaned[Quantité])