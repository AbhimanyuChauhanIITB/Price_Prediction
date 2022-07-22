# -*- coding: utf-8 -*-
"""200040006_Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14mmgR0iazO4Z5wXaM4r_jJxGUkXvH9kP
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
restaurent_data=pd.read_csv('/content/drive/MyDrive/restaurent.csv')
restaurent_data.describe()

import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame(restaurent_data)
df=df.sample(n=50)
service=df.iloc[:,2]
decor=df.iloc[:,1]
food=df.iloc[:,0]
price=df.iloc[:,3]

"""a)Plots between price and other variables.

"""

plt.scatter(y=price,x=food)
plt.show()
plt.scatter(y=price,x=service)
plt.show()
plt.scatter(y=price,x=decor)
plt.show()

"""b)Multivariate regression on the given variables vs price.

"""

index=np.arange(1,51) 
theta = [0] * 4
L=0.0001
pr=df.iloc[:,3]
x0=df.iloc[:,0]
x1=df.iloc[:,1]
x2=df.iloc[:,2]
X=np.array([x0,x1,x2,1])
n=float(len(x0))
epochs=2000
for i in range(epochs):
    y_prd=sum(theta*X)
    for j in range(0,4):
        theta[j]=theta[j]+(L*(1/n)*sum((pr-y_prd)*X[j]))
       
        
print("w1=",theta[1],"w2=",theta[2],"w3=",theta[3],"b=",theta[0])   
print("Predicted Price=",(theta[1]*125)+(theta[2]*265)+(theta[3]*148)+theta[0])

"""c)Coefficients from multivariate."""

y_prd=(sum(theta*X)) 
      
plt.plot(index,pr,color='black')
plt.plot(index,y_prd,color='red')
plt.show()

"""d)Linear regression on price vs food. Plot of food vs service.
In linear regression the values found for the coefficient are different from those of multivariate regression as expected because multivariate takes all the variables into account.
"""

plt.scatter(y=service,x=food,color='green')
plt.show()

m=0
c=0
L=0.0001
n=float(len(food))
epochs=1000
for i in range(epochs): 
    price_pred = m*food + c  
    D_m = (-2/n) * sum(food * (price - price_pred))  
    D_c = (-2/n) * sum(price - price_pred)  
    m = m - L * D_m  
    c = c - L * D_c  
print("w1=",m,"b=",c)

price_pred1=m*125+c
    print(price_pred1)

price_pred=m*food+c
plt.scatter(food,price)
plt.plot(food,price_pred,color='green')
plt.show()

print(theta)

"""e)food=20, service=3 and decor=17 price prediction."""

print("Predicted Price=",(theta[1]*20)+(theta[2]*17)+(theta[3]*3)+(theta[0]))

