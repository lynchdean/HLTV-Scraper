import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# dataset headers
names = ['match_id', 'team_name', 'player_name', 'kills', 'assists', 'flash_assists', 'deaths', 'kd_ratio', 'kd_diff',
         'adr', 'fk_dif', 'rating']

csv_path = 'data2.csv'
df = pd.read_csv(csv_path, names=names)

# Preproccessing
X = df.iloc[:, 3:].values
y = df.iloc[:, 1].values

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# Feature scaling
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Training and Predictions
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Evaluation
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Accuracy
print(classifier.score(X_test, y_test))
