import pandas as pd
from sklearn.preprocessing import LabelEncoder

class DataProcessor:
    #Reads data
    def read_data(path):

        if path.lower().endswith('.csv'):
            data = pd.read_csv(path)
        elif path.lower().endswith('.xlsx'):
            data = pd.read_excel(path)
        elif path.lower().endswith('.json'):
            data = pd.read_json(path)
        else:
            raise ValueError("unsupported data file")

        return data

    #data summary
    def summarize_data(data):
        return data.describe()

    #Handles missing values
    def handle_missing_values(data):

        data.dropna(inplace=True)
        data.fillna(data.mean(), inplace=True)

    #Encoding categorical columns
    def encode_categorical_columns(data):

        label_encoder = LabelEncoder()
        for column in data.select_dtypes(include=['object']).columns:
            data[column] = label_encoder.fit_transform(data[column])

        return data

#example to try the code:
"""
file_path = "your_data.csv"  # Replace with the actual file path
processor = DataProcessor()
data = processor.read_data(file_path)
summary = processor.summarize_data(data)
print(summary)
processor.handle_missing_values(data)
encoded_data = processor.encode_categorical_columns(data)
print(encoded_data)

"""


"""
here is one of my projects that I applied data processing on the data to use AI model:
https://www.kaggle.com/code/baraamelhem/titaniccomp 
"""