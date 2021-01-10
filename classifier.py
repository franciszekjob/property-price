from sklearn.neighbors import KNeighborsClassifier
from pickle import dump
import pandas as pd
import numpy as np

np.set_printoptions(suppress=True)

df = pd.read_csv('data_scraper/property_data_prep.csv')
features = []
labels = []

for i in range(len(df['price'])):
    features.append(np.array([
        int(df['location'][i]),
        float(df['area'][i]),
        int(df['year'][i]),
        int(df['rooms'][i]),
        int(df['level'][i]),
        int(df['state'][i])
    ]))
    labels.append(int(df['price'][i]))
features = np.array(features)
labels = np.array(labels)

clf = KNeighborsClassifier()
clf.fit(features, labels)
pkl_name = "pickle_model_v3.pkl"
with open(pkl_name, 'wb') as file:
    dump(clf, file)
