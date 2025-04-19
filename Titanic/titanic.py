import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder

titanic = pd.read_csv ("train.csv")
titanic.info()

X = titanic.iloc[:, :-1].values
y = titanic.iloc[:, -1].values
#print(X)
print(y)

print('Finish')