# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
df=pd.read_excel('comparison_students.xlsx')
df.columns = df.iloc[0]
df=df.drop(0)
df=df.reset_index(drop=True)
x=df[['English Question Attempt','English Total Marks','English Scores','English PCT']]
y=df['English Level']
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=12345)
model = DecisionTreeClassifier(criterion='entropy',max_depth=5)
model.fit(x_train,y_train)

pickle.dump(model,open('model1.pkl','wb'))

model=pickle.load(open('model1.pkl','rb'))
print(model.predict([[7,7,5,71]]))
print(np.percentile(x,70))