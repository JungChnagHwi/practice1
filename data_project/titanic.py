import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
# print(train.head(10))
# print(test.head(10))
train = pd.DataFrame(train)
test = pd.DataFrame(test)
# train.info()
# print(train.describe())

from sklearn.preprocessing import LabelEncoder
test_p = test.iloc[:, 0]
train_p = train.iloc[:,1]
train = train.iloc[:, [2,4,5,6,7,10,11]]
test = test.iloc[:,[1,3,4,5,6,9,10]]

train.loc[:, ["Sex","Cabin", "Embarked"]] = train.loc[:,["Sex","Cabin", "Embarked"]].apply(LabelEncoder().fit_transform)
test.loc[:, ["Sex","Cabin", "Embarked"]] = test.loc[:,["Sex","Cabin", "Embarked"]].apply(LabelEncoder().fit_transform)

m1 = train["Age"].mean()
m2 = test["Age"].mean()

train["Age"] = train["Age"].fillna(m1)
test["Age"] = test["Age"].fillna(m2)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(train, train_p,test_size=0.2, random_state=42, stratify=train_p)

md = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=4)
md.fit(x_train, y_train)
print(md.score(x_train, y_train))
print(md.score(x_test, y_test))

pred1 = md.predict_proba(x_test)
pred1 = pd.DataFrame(pred1)
pred1 = pred1.iloc[:, 1]
#print(pred1)

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, f1_score, roc_auc_score
print(roc_auc_score(y_test, pred1))

pred = md.predict_proba(test)
pred = pd.DataFrame(pred)
pred = pred.iloc[:, 1]
#print(pred)

res = pd.concat([test_p, pred], axis=1)
res = pd.DataFrame({'고객':test_p, '생존':pred})
print(res)

res.to_csv('타이타닉1.csv', index=False)