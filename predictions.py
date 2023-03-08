import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import DB

# connect to database and load historical data
data = DB.get_plant_data()

# preprocess data
data = data.dropna()
data = data.drop_duplicates()
data = data.reset_index(drop=True)

# extract features and labels
X = data[['temp_air', 'temp_soil', 'moisture_air', 'moisture_soil', 'light_level']]
y = data['needs_water']
# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# train decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# evaluate accuracy of classifier
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# predict if plant needs watering in next hour
temp_air = db_conn.get_latest_value('temp_air')
temp_soil = db_conn.get_latest_value('temp_soil')
moisture_air = db_conn.get_latest_value('moisture_air')
moisture_soil = db_conn.get_latest_value('moisture_soil')
light_level = db_conn.get_latest_value('light_level')
X_new = np.array([[temp_air, temp_soil, moisture_air, moisture_soil, light_level]])
y_new = clf.predict(X_new)
if y_new == 1:
    print("Plant needs watering in next hour")
else:
    print("Plant does not need watering in next hour")
