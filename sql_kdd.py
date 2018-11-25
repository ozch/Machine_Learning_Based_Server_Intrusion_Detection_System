from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sqlalchemy import create_engine
import pymysql
from mysql_connection import *
import pandas as pd
import numpy as np
db_con = MySQLConnection()
conn = db_con.getConnection()

#df = pd.read_sql("select srv_count,src_bytes,count,label from kdd where service='ecr_i'",conn)
df = pd.read_sql("select srv_count,src_bytes,count,label from kdd where service='ecr_i' and (label='normal' or label='smurf')",conn)

df["label"].replace("smurf",1,inplace=True)
df["label"].replace("pod",1,inplace=True)
df["label"].replace("nmap",1,inplace=True)
df["label"].replace("ipsweep",1,inplace=True)
df["label"].replace("portsweep",1,inplace=True)
df["label"].replace("normal",0,inplace=True)

label = np.array(df.pop("label"))
features = np.array(df)

print("Splitting Data")
X_train,X_test,y_train,y_test = train_test_split(features,label,shuffle=True,random_state=66)

print("Training Model..")
model = GaussianNB()
model.fit(X_train,y_train)

print("Train Accuracy : ", model.score(X_train, y_train))
print("Test Accuracy : ", model.score(X_test, y_test))
perdict = model.predict([X_test[0]])
print(perdict)
print(y_test[0])

y_pred = model.fit(X_train, y_train).predict(X_test)
cnf_matrix = confusion_matrix(y_test, y_pred)
print(cnf_matrix)
