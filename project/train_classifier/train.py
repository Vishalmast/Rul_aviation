import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import pickle

train_df = pd.read_csv("../../CMaps/train_FD001.txt",sep=" ",header=None)
test_df = pd.read_csv("../../CMaps/test_FD001.txt", sep = " ", header = None)
df = train_df

columns = ['unit_number','time_in_cycles','setting_1','setting_2','TRA','T2','T24','T30','T50','P2','P15','P30','Nf',
           'Nc','epr','Ps30','phi','NRf','NRc','BPR','farB','htBleed','Nf_dmd','PCNfR_dmd','W31','W32', "26", "27" ]
df.columns = columns
test_df.columns = columns
df.drop(['26', '27'], axis = 1,  inplace = True)
test_df.drop(['26', '27'], axis = 1,  inplace = True)
df.drop(['setting_1', 'TRA', 'P30', 'phi', 'farB', 'Nf_dmd', 'PCNfR_dmd', 'W31', 'W32'], axis = 1,  inplace = True)
test_df.drop(['setting_1', 'TRA', 'P30', 'phi', 'farB', 'Nf_dmd', 'PCNfR_dmd', 'W31', 'W32'], axis = 1,  inplace = True)
y = df['time_in_cycles']
x = df.drop('time_in_cycles', axis = 1)
y_test = test_df['time_in_cycles']
x_test = test_df.drop('time_in_cycles', axis = 1)

reg = LinearRegression()
reg.fit(x, y)

polynomial_features= PolynomialFeatures(degree=2)
x_poly = polynomial_features.fit_transform(x)
x_poly_test = polynomial_features.fit_transform(x_test)
# model.score(x_poly_test, y_test)
filename = 'model1.pkl'
pickle.dump(reg, open(filename, 'wb'))
