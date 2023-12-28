# -*- coding: utf-8 -*-
"""Netflix Data analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FgPeMiPBLxVZAQr1V0tEF8lCJ6xVdOc3
"""

import numpy as np
import pandas as pd

data = pd.read_csv("/content/file.csv")

data.head()

data.tail()

data.shape

data.size

list(data.columns)

data.dtypes

data.info()

data[data.duplicated()]

data.drop_duplicates(inplace = True)

data.shape

data.head()

data.isnull()

data.isnull().sum()

import seaborn as sns

sns.heatmap(data.isnull())

data.head()

data[data['Title'].isin(["House of Cards"])]

data[data['Title'].str.contains("House of Cards")]

data.dtypes

data['Date_N'] = pd.to_datetime(data["Release_Date"])

data.head()

data.dtypes

data["Date_N"].dt.year.value_counts()

data["Date_N"].dt.year.value_counts().plot(kind='bar')

data.head(2)

data.groupby('Category').Category.count()

import matplotlib.pyplot as plt
sns.countplot(x="Category",data=data)
plt.show()

data.head(2)

data['Year']=data["Date_N"].dt.year

data.head(2)

data[(data['Category']=="Movies") & (data['Year']==2000)]

data[(data["Category"]=="Movie")& (data['Year']==2020)]

data.head(2)

data[(data["Category"]=="TV Show")&(data["Country"]=="India")]['Title']

data.head(2)

data["Director"].value_counts().head(10)

data.head(2)

data[(data["Category"]=="Movie")&(data["Type"]=="Comedies")]

data[(data["Category"]=="Movie")&(data["Type"]=="Comedies") |(data["Country"]=="United Kingdom")]

data.head(2)

data[data["Cast"]=="Tom Cruise"]

data[data["Cast"].str.contains("Tom Cruise")]

data_new = data.dropna()

data_new[data_new["Cast"].str.contains("Tom Cruise")]

data.nunique()
data.head(2)

data["Rating"].nunique()

data["Rating"].unique()

data.head(2)

data[(data["Category"]=="Movie")&(data["Rating"]=="TV-14")& (data["Country"]=="Canada")]

data[(data["Category"]=="Movie") & (data["Rating"]=="TV-14") & (data["Country"]=="Canada")].shape

data[(data["Category"]=="TV Show") & (data["Rating"]=="R") & (data["Year"]>2018)]

data.head(2)

data["Duration"].unique()

data.Duration.dtypes

data[["Minutes","Unit"]] = data["Duration"].str.split(" ",expand = True)

data.head(2)

data.Minutes.max()

data.Minutes.min()

data.Minutes.mean()

data.head(2)

data_tvshow = data[data["Category"]=="TV Show"]

data_tvshow.head()

data_tvshow.Country.value_counts().head(1)

data.sort_values(by = "Year").head(2)

data.sort_values(by = "Year",ascending = False).head(2)

data[(data["Category"]=="Movie") & (data["Type"]=="Dramas")|(data["Category"]=="TV Show")&(data["Type"]=="Kids'TV")]

