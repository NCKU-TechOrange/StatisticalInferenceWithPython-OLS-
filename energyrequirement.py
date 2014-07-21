
# coding: utf-8

# In[1]:

import pandas as pd
from pandas import Series, DataFrame
import pylab 
get_ipython().magic('pylab inline')
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm


# In[2]:

energy = pd.read_csv('/Users/tzeng/Desktop/data_energy.csv')
energy


# In[3]:

Wt = energy.Wt.tolist()
Energy = energy.Energy.tolist()


# In[4]:

# Descriptive Statistics
# sample mean of energy requirements(Y) and weights(X)
x_bar = 0
for i in Wt:
    x_bar = x_bar + i
x_bar = x_bar/len(Wt)
print(x_bar)

y_bar = 0
for i in Energy:
    y_bar = y_bar + i
y_bar = y_bar/len(Energy)
print(y_bar)


# In[5]:

# first : construct the background
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# second : add point into it.
ax.scatter(Wt, Energy)
ax.scatter(x_bar,y_bar,color='red')
ax.set_xlabel('Weight of sheep')
ax.set_ylabel('energy requirements')
ax.set_title('Scatter plot between Weight and Energy requirements')


# In[6]:

# run an OLS regression analysis
result = sm.ols(formula='Energy ~ Wt', data=energy)
fitted = result.fit()
print (fitted.summary())


# In[7]:

# put the estimated parameters into the model
a = 0.0434
b = 0.1329
energy_fit = []
for i in Wt:
    i = i * a + b
    energy_fit.append(i)
energy_fit2 = []

#for i in Wt:
#    i = i * a 
#    energy_fit2.append(i)


# In[8]:

# put the fitted line into the plot
# first : construct the background
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
# second : add point into it.
ax.scatter(Wt, Energy)
ax.plot(Wt,energy_fit,color='green')
ax.scatter(x_bar,y_bar,color='red')
ax.set_xlabel('Weight of sheep')
ax.set_ylabel('energy requirements')
ax.set_title('Scatter plot between Weight and Energy requirements')


# In[9]:

#residual
res = []
for i in range(len(Energy)):
    res.append(Energy[i]-energy_fit[i])
res
#residual plot
fig = plt.figure() 
ax = fig.add_subplot(1,1,1)
ax.scatter(energy_fit, res)





