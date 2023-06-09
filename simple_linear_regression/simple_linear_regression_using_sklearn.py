import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score , mean_squared_error
from math import sqrt
x = [1 , 2 , 3 , 4 , 5]
y = [3 , 4 , 2 , 4 , 5]

x = np.array(x).reshape(-1 , 1)
y = np.array(y)

model = LinearRegression()


xtrain , xtest , ytrain , ytest = train_test_split(x , y , test_size=0.2 , random_state= 42)
model.fit(xtrain , ytrain)

def rmse(true_val , pred_val):
   score =  sqrt(mean_squared_error(true_val , pred_val))
   print(f' the rmse score is : {score}')

y_pred  = model.predict(xtest)
# print(y_pred)
score = rmse(ytest , y_pred)

