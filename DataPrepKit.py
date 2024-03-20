import pandas as pd

# Data Reading
data=pd.read_csv(path)
data=pd.read_excel(path)
data=pd.read_json(path)

# Data Summary
data.describe()

#Handling Missing Values
data.dropna()
data.fillna(data.mean())

#Categorical Data Encoding
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
for column in dataframe.select_dtypes(include=['object']).columns:
    dataframe[column] = label_encoder.fit_transform(dataframe[column])
return dataframe


# here is one of my projects that I applied data processing on the data to use AI model:
# https://www.kaggle.com/code/baraamelhem/titaniccomp 