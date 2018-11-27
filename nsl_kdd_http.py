from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split, KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import *
import pickle
import pandas as pd
import numpy as np

from k_fold_validation import KFoldValidation

model_cat = "http"
#mapping to mathematical values
flag_map = {'S0':0,'S1':1,'S2':2,'S3':3,'SH':4,'SF':5,'OTH':6,'REJ':7,'RSTO':8,'RSTR':9,'RSTOS0':10}
class_map = {'normal':0,'anomaly':1}
#reading csv data
csv = pd.read_csv("data\\HTTP.csv")
columns=["'duration'","'flag'","'service'","'src_bytes'","'dst_bytes'","'urgent'","'wrong_fragment'","'class'"]
df = pd.DataFrame(csv,columns=columns)

#data manipulation, quering required data
df1 = df.loc[df["'service'"]=='http']
df2 = df.loc[df["'service'"]=='http_443']
df = pd.concat([df1,df2])

df["'flag'"].replace(flag_map,inplace=True)
df["'class'"].replace(class_map,inplace=True)
print(df)

#slice and dice.
df.pop("'service'")
label = np.array(df.pop("'class'"))
features = np.array(df)
X_train,X_test,y_train,y_test = train_test_split(features,label,shuffle=True,random_state=77)

#training model
print("Training Model..")
model = GaussianNB()
model.fit(X_train,y_train)

#saving model using pickle
m_name="gnb"
pkl_filename="models\\"+model_cat+"_"+m_name+'.pkl'
with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)

#accuracy calculation
print("Train Accuracy : ", model.score(X_train, y_train))
print("Test Accuracy : ", model.score(X_test, y_test))

#testing data through perdiction
perdict = model.predict([X_test[200]])
print(perdict)
print(y_test[200])

try:
    # confusion matrix
    y_pred = model.fit(X_train, y_train).predict(X_test)
    cnf_matrix = confusion_matrix(y_test, y_pred)
    print(cnf_matrix)
except:
    y_pred = model.fit(X_train.round(), y_train.round()).predict(X_test.round())
    cnf_matrix = confusion_matrix(y_test.round(), y_pred.round())
    print(cnf_matrix)

kf = KFoldValidation()
kf.GetAverageScore(10,features,label,GaussianNB(),X_train)