import pandas as pd
import seaborn as sns

# Load the data se
dataset = "heart_Dataset/heart_disease_data.csv"
column_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal','class']

dataset = pd.read_csv(dataset, names=column_names)

#drop rows with NaN values from DataFrame
dataset = dataset.dropna(axis=0)
dataset = dataset.dropna(axis=1)


print(dataset.head(7))  # Print the first 7 row
print(dataset.shape)  # Get the shape of the data (the number of rows & columns)
print(dataset.isna().sum())  # Count the empty (NaN, NAN, na) values in each column
print(dataset.describe())  # View some basic statistical details like percentile, mean, standard deviation etc.

# Split the dataset into 'feature-data' and 'target-data'
feature_data = dataset.iloc[:, :-1].values
target_data = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(feature_data, target_data, test_size= 0.25, random_state = 1)  # Split the data again, into 75% training data set and 25% testing data set.

# Use Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=1)
forest.fit(X_train, Y_train)

#Test the models accuracy on the trainingg data set
model = forest
print(model.score(X_train, Y_train))

# saving module
import joblib
joblib.dump(model, 'model-heart_disease.joblib')