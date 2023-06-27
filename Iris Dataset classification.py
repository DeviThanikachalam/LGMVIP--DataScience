
import pandas as pd
dataset=pd.read_csv('iris.csv')
dataset
import pandas as pd
dataset=pd.read_csv('iris.csv')
dataset
dataset.shape

dataset.head
dataset.head(10)
dataset.tail()
dataset.tail(10)

dataset.columns

dataset['variety']

dataset.dtypes

dataset.describe()

dataset.iloc[:,:]

dataset.iloc[0:20,:]

dataset.iloc[0:20,1:3]

dataset[dataset['sepal.length']>7]

dataset[(dataset['sepal.length']>7)&(dataset['petal.width']==2.1)]

dataset.isna().sum()

dataset['variety'].value_counts()

