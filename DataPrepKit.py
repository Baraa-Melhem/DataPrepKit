import pandas as pd
from sklearn.preprocessing import LabelEncoder

class DataProcessor:
    def read_data(path):
# Reading data 
        if path.lower().endswith('.csv'):
            data = pd.read_csv(path)
        elif path.lower().endswith('.xlsx'):
            data = pd.read_excel(path)
        elif path.lower().endswith('.json'):
            data = pd.read_json(path)
        else:
            raise ValueError("Unsupported data file format")

        return data
#summarizing data
    def summarize_data(data):
        return data.describe()
#handle with missing data
    def handle_missing_values(data):

        data.dropna(inplace=True)
        data.fillna(data.mean(), inplace=True)
# encoding categorical columns
    def encode_categorical_columns(data):
        label_encoder = LabelEncoder()
        for column in data.select_dtypes(include=['object']).columns:
            data[column] = label_encoder.fit_transform(data[column])

        return data

# to try the code :
"""
file_path = "data.csv"  
processor = DataProcessor()
data = processor.read_data(file_path)
summary = processor.summarize_data(data)
print(summary)
processor.handle_missing_values(data)
encoded_data = processor.encode_categorical_columns(data)
print(encoded_data)
"""

"""
here is one of my projects that I applied data processing on the data to use it to train my AI model:
https://www.kaggle.com/code/baraamelhem/titaniccomp 
"""
