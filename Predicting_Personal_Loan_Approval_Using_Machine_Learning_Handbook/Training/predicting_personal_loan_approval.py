# -*- coding: utf-8 -*-
"""Predicting_Personal_Loan_Approval

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kDY39LbrI1HnTwndyZ-NZCxK3yVu0jHR
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
import imblearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix, f1_score

#importing the dataset which is in csv file
data = pd.read_csv('/content/test.csv')
data = pd.read_csv('/content/train.csv')
data

data.drop(['Loan_ID'],axis=1,inplace=True)

data.head()

data['Gender']=data['Gender'].map({'Female':1,'Male':0})
data.head()

data['Property_Area']=data['Property_Area'].map({'Urban':2,'Semiurban': 1,'Rural':0})
data.head()

data['Married']=data['Married'].map({'Yes':1,'No':0})
data.head()

data['Education']=data['Education'].map({'Graduate':1,'Not Graduate':0})
data.head()

data['Self_Employed']=data['Self_Employed'].map({'Yes':1,'No':0})
data.head()

data['Loan_Status']=data['Loan_Status'].map({'Y':1,'N':0})
data.head()

data.isnull().sum()

data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])

data['Married'] = data['Married'].fillna(data['Married'].mode()[0])

data['Dependents'] = data['Dependents'].str.replace('+','')

data['Dependents'] = data['Dependents'].fillna(data['Dependents'].mode()[0])

data['Self_Employed'] = data['Self_Employed'].fillna(data['Self_Employed'].mode()[0])

data['LoanAmount'] = data['LoanAmount'].fillna(data['LoanAmount'].mode()[0])

data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0])

data['Credit_History'] = data['Credit_History'].fillna(data['Credit_History'].mode()[0])

data.isnull().sum()

data.info()

data['Gender'] = data['Gender'].astype('int64')
data['Married'] = data['Married'].astype('int64')
data['Dependents'] = data['Dependents'].astype('int64')
data['Self_Employed'] = data['Self_Employed'].astype('int64')
data['CoapplicantIncome'] = data['CoapplicantIncome'].astype('int64')
data['LoanAmount'] = data['LoanAmount'].astype('int64')
data['Loan_Amount_Term'] = data['Loan_Amount_Term'].astype('int64')
data['Credit_History'] = data['Credit_History'].astype('int64')

data.info()

plt.figure(figsize=(12,5))
plt.subplot(121)
sns.distplot(data['ApplicantIncome'], color='r')
plt.subplot(122)
sns.distplot(data['Credit_History'])
plt.show()

plt.figure(figsize=(18,4))
plt.subplot(1,4,1)
sns.countplot(x = 'Gender',data = data)
plt.subplot(1,4,2)
sns.countplot(x = 'Education',data = data)
plt.show()

plt.figure(figsize=(20,5))
plt.subplot(131)
sns.countplot(x = 'Married', hue = 'Gender', data = data)
plt.subplot(132)
sns.countplot(x = 'Self_Employed', hue = 'Education', data = data)
plt.subplot(133)
sns.countplot(x = 'Property_Area', hue = 'Loan_Amount_Term', data = data)

pd.crosstab(data['Gender'],[data['Self_Employed']])

sns.swarmplot(x = "Gender",y = "ApplicantIncome", hue = "Loan_Status", data = data)

from imblearn.combine import SMOTETomek

smote = SMOTETomek()

y = data['Loan_Status']
x = data.drop(columns=['Loan_Status'],axis=1)

x.shape

y.shape

x_bal,y_bal = smote.fit_resample(x,y)

print(y.value_counts())
print(y_bal.value_counts())

data.describe()

names=x_bal.columns

x_bal.head()

sc=StandardScaler()
x_bal=sc.fit_transform(x_bal)

x_bal

x_bal = pd.DataFrame(x_bal,columns=names)
x_bal.head()

x_train, x_test, y_train, y_test = train_test_split(
    x_bal, y_bal, test_size=0.33, random_state=42)

x_train.shape

x_test.shape

y_train.shape, y_test.shape

def decisionTree(x_train,x_test,y_train,y_test):
    dt=DecisionTreeClassifier()
    dt.fit(x_train,y_train)
    yPred = dt.predict(x_test)
    print('***DecisionTreeClassifier***')
    print('Confusion matrix')
    print(confusion_matrix(y_test,yPred))
    print('Classification report')
    print(classification_report(y_test,yPred))

def randomForest(x_train,x_test,y_train,y_test):
    rf = RandomForestClassifier()
    rf.fit(x_train,y_train)
    yPred = rf.predict(x_test)
    print('***RandomForestClassifier***')
    print('Confusion matrix')
    print(confusion_matrix(y_test,yPred))
    print('Classification report')
    print(classification_report(y_test,yPred))

def KNN(x_train,x_test,y_train,y_test):
    dt = KNeighborsClassifier()
    knn.fit(x_train,y_train)
    yPred = knn.predict(x_test)
    print('***KNeighborsClassifier***')
    print('Confusion matrix')
    print(confusion_matrix(y_test,yPred))
    print('Classification report')
    print(classification_report(y_test,yPred))

def xgboost(x_train,x_test,y_train,y_test):
    xg = GradientBoostingClassifier()
    xg.fit(x_train,y_train)
    yPred = xg.predict(x_test)
    print('***GradientBoostingClassifier***')
    print('Confusion matrix')
    print(confusion_matrix(y_test,yPred))
    print('Classification report')
    print(classification_report(y_test,yPred))

import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(units=100, activation='relu', input_dim=11))

classifier.add(Dense(units=50, activation='relu'))

classifier.add(Dense(units=1, activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])

model_history = classifier.fit(x_train, y_train, batch_size=100, validation_split=0.2, epochs=100)

y_pred = classifier.predict(x_test)

y_pred

y_pred = (y_pred > 0.5)
y_pred

print(accuracy_score(y_pred, y_test))
print("ANN Model")
print("Confusion_Matrix")
print(confusion_matrix(y_test, y_pred))
print("Classification Report")
print(classification_report(y_test, y_pred))

rf = RandomForestClassifier()

parameters = {
               'n_estimators' : [1,20,30,55,68,74,90,120,115],
                'criterion':['gini','entropy'],
                'max_features' : ["auto", "sqrt", "log2"],
        'max_depth' : [2,5,8,10], 'verbose' : [1,2,3,4,6,8,9,10]
}

RCV  = RandomizedSearchCV(estimator=rf,param_distributions=parameters,cv=10,n_iter=4)

RCV.fit(x_train,y_train)

bt_params = RCV.best_estimator_
bt_score = RCV.best_score_

bt_params

bt_score

def RandomForest(x_train,x_test,y_train,y_test):
    model = RandomForestClassifier(verbose= 4, n_estimators= 68,max_features= 'auto',max_depth= 8,criterion= 'entropy')
    model.fit(x_train,y_train)
    y_tr = model.predict(x_train)
    print("Training Accuracy")
    print(accuracy_score(y_tr,y_train))
    yPred = model.predict(x_test)
    print('Testing Accuracy')
    print(accuracy_score(yPred,y_test))

model = RandomForestClassifier(verbose= 4, n_estimators= 68,max_features= 'auto',max_depth= 8,criterion= 'entropy')
model.fit(x_train,y_train)

RandomForest(x_train,x_test,y_train,y_test)

pickle.dump(model,open('rdf.pkl','wb'))

pickle.dump(sc,open('scale.pkl','wb'))

from flask import Flask
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open(r'rdf.pkl', 'rb'))
scale = pickle.load(open(r'scale.pkl', 'rb'))

@app.route('/') # rendering the html templet
def home():
  return render_template('home.html')

@app.route('/submit',methods=["POST","GET"])# route to show the prediction in a UI
def submit():
  # reading the inputs given by the user
  input_feature=[int(X) for x in request.form.value()]
  #input_feature = np.transpose(input_feature)
  input_feature=[np.array(input_feature)]
  print(input_feature)
  names = ['Gender', 'Married', 'Departments', 'Education', 'Self_Empolyed', 'ApplicantIncome', 
           'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History','Property_Area']
  print(data)




   # predictions using the loaded model file
  prediction=model.predict(date)
  print(prediction)
  prediction = int(prediction)
  print(type(prediction))

  if (prediction == 0):
      return render_template("output.html",result ="Loan will Not be Approved")
  else:
      return render_template("output.html",result = "Loan will be Approved")
  # showing the prediction results in a UI

if __name__=="__main__":
  def os():
   # app.run(host='0.0.0.0', port=8000,debug=True)   # running the app
   port=int(os.environ.get('PORT',5000))
   app.run(debug=False)