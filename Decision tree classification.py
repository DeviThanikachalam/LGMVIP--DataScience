#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
data=pd.read_csv('iris.csv')
print(data.head())
x=data[['sepal.length','sepal.width','petal.length','petal.width']]
y=data['variety']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
model=tree.DecisionTreeClassifier()
model.fit(x_train,y_train)
print('Score: ',model.score(x_test,y_test))
print('Predicted as: ',model.predict([[4.4,2.9,1.4,0.2]]))
tree.plot_tree(model)


# In[ ]:





# In[ ]:




