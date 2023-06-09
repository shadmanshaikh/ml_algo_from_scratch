'''
Authors Name : shadman
Date : 5-5-23
Description : Implementing simple linear regression from scratch ( without using any built in library )

'''

# Y = m * x + c
# where y is dependent variable and x is independent variable

x = [1 , 2 , 3 , 4 , 5]
y = [3 , 4 , 2 , 4 , 5]

# finding the values of m and c

# first find the mean of both y and x
if len(x) ==  len(y):
    n = len(x)
    
x_sum = 0
y_sum = 0
for i in range(0,n):
    x_sum += x[i]
    y_sum += y[i]
    # print("value of X: ",x_sum)
x_mean = x_sum/n 
y_mean = y_sum/n
# y_sum = 0
# for j in range(0,len(y)):
#     y_sum += y[j]    
    # print("value of Y: ",y_sum)
numerator = 0
denominator = 0
n = len(x)
for i in range(n):
    # for j in range(0,len(y)):
        xdiff = (x[i] - x_mean)
        ydiff = (y[i] - y_mean)
        numerator +=  xdiff * ydiff
        denominator += (x[i] - x_mean)**2

# therefore the m value is numerator by denominator
m = numerator / denominator
# print(f'numerator val : {numerator} , denominator val: {denominator}')
print(f'the value of m is : {m}')

# find the value of c 
# we know that y = m*x + c
# we can change it into c = (m * xmean) - ymean , to get c val

c =  y_mean - (m * x_mean) 
print(f'the value of c is : {c}')

# the predict the ypred val , as ypred = m*x + c

# for i in range(0,n):
#     print(y_pred)

# to find the how close the data are fitted in the regression line we use R2 value

r2_numerator = 0
r2_denominator = 0
# r2 =
sample_y = []
for i in range(0,n):
    y_pred = m * x[i] + c
    sample_y.append(y_pred)
    r2_numerator += (y_pred - y_mean)**2
    r2_denominator += (y[i] - y_mean)**2
    # print(r2_numerator)
r2 = r2_numerator / r2_denominator

print(f'the r2 value is : {r2}')


import numpy as np
min_x = np.min(y) - 100
max_x = np.min(x) + 100
print(f'{min_x} , {max_x}')


import matplotlib.pyplot as plt

X = np.linspace(min_x , max_x , 100)
plt.plot(x , sample_y , color = "blue" , label = "regression line")
plt.scatter(x , y , color ="red" , label = "data points")
plt.show()
