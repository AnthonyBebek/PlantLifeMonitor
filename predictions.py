import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import DB

data = DB.get_plant_data()

data = data.dropna()
data = data.drop_duplicates()
data = data.reset_index(drop=True)

X = data[['temp_air', 'temp_soil', 'moisture_air', 'moisture_soil', 'light_level']]
y = data['needs_water']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

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
