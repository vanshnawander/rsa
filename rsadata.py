import pandas as pd
import pymysql
import csv
try:
        connection = pymysql.connect(host='localhost',user='root',password='######',db='rsa',autocommit=True)
        cursor = connection.cursor()
        print("databasse connected")
except Exception as e:
        print("database failed to connect")
        print("error : ",e)
cursor.execute("select * from `rsa`.`RSA_Parameters`")
data=cursor.fetchall()
p=[]
q=[]
ni=[]
phi=[]
e=[]
d=[]
for i,j,k,l,m,n in data:
        p.append(i)
        q.append(j)
        ni.append(k)
        phi.append(l)
        e.append(m)
        d.append(n)
dic = {"prime_P":p ,"Prime_Q" : q ,"n(p*q)":ni ,"phi":phi,"public_key_E":e,"private_key_D":d}
df=pd.DataFrame(dic,dtype=pd.StringDtype())
dica = {"prime_P":str ,"Prime_Q" : str ,"n(p*q)":str ,"phi":str,"public_key_E":str,"private_key_D":str}
df = df.astype(pd.StringDtype())
print(df.dtypes)
print(df)
csv=df.to_csv("F:/rsa_dataset.csv",float_format=str,quoting=csv.QUOTE_NONNUMERIC)
