# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 19:16:17 2016

@author: Aditya
"""

import pandas as pd
import numpy as np
from sklearn import cross_validation, neighbors

df = pd.read_csv('transfusion.data.txt')
#df = df.drop(['months'],1)


X = np.array(df.drop(['donated'],1))
y = np.array(df['donated'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy=clf.score(X_test, y_test)
print(accuracy)