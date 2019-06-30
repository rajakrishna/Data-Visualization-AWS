# """Cloud Foundry test"""
# from flask import Flask,render_template,request
# import os
# import pyodbc
# import csv

# app = Flask(__name__)



# @app.route('/')
# def home():
#   return render_template("home.html")

# @app.route('/showdb5', methods=['GET', 'POST'])
# def showdb5():
#     cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT StateName from voting where TotalPop between 5000 and 10000 ")
#     row = cursor.fetchall()
#     return render_template("showdb.html", row=row)

# @app.route('/showdb10', methods=['GET', 'POST'])
# def showdb10():
#     cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT StateName from voting where TotalPop between 10000 and 50000 ")
#     row = cursor.fetchall()
#     return render_template("showdb.html", row=row)



# # @app.route('/magsearch', methods=['GET', 'POST'])
# # def magsearch():
# #     mag1 = request.form['mag1']
# #     mag2 = request.form['mag2']
# #     con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# #     query="Select mag,latitude from quake3 where mag between '"+mag1+"' and '"+mag2+"'"
# #     columns=['mag','latitude']
# #     dic=dict()
# #     cur=con.cursor()
# #     mem=[]
# #     cur.execute(query)
# #     result=list(cur.fetchall())
# #     for row in result:
# #         memdict=dict()
# #         for j,val in enumerate(row):
# #             memdict[columns[j]]=val
# #         mem.append(memdict)
# #     # a=[1,2,3,4,5]
# #     return render_template('chart.html',a=mem,chart="pie")

# # @app.route('/magsearch', methods=['GET', 'POST'])
# # def magsearch():
# #     mag1 = request.form['mag1']
# #     mag2 = request.form['mag2']
# #     con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
# #     query="Select mag,latitude from quake3 where mag between '"+mag1+"' and '"+mag2+"'"
# #     columns=['mag','latitude']
# #     dic=dict()
# #     cur=con.cursor()
# #     mem=[]
# #     cur.execute(query)
# #     result=list(cur.fetchall())
# #     for row in result:
# #         memdict=dict()
# #         for j,val in enumerate(row):
# #             memdict[columns[j]]=val
# #         mem.append(memdict)
# #     # a=[1,2,3,4,5]
# #     return render_template('barchart.html',a=mem,chart="bar")


# @app.route('/piechart', methods=['GET', 'POST'])
# def piechart():
#     n1 = int(request.form['n1'])
#     n2 = int(request.form['n2'])
#     mem=[]
#     for y in range(n1,n2,1):
#      memdict=dict()
#      x=y*y+1 
#      memdict['xaxis']=x
#      memdict['yaxis']=y
#      mem.append(memdict)
#     return render_template('chart_karthik.html',a=mem,chart="scatter")

# port = int(os.getenv("PORT", 5000))
# if __name__ == '__main__':
#     app.run(port=port,debug=True)

import os
import pandas as pd
import numpy as np
import csv
from flask import Flask,render_template,request
from sklearn.cluster import KMeans
from array import array
import matplotlib.pyplot as plt
import itertools
import math
import time

application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("home.html")
    
@application.route('/cluster', methods=['GET', 'POST'])
def cluster():
    # mylist = []
    # attr1 = 3
    # attr2 = 9
    clus  = request.form['n']
    s = time.time()
    tag1 = int(clus)
    df1 = pd.read_csv("minnowc.csv")
    df1.CabinNum *= 0.01  
    df2 = df1[['Age', 'Fare']]
    df = df2.dropna().to_numpy()

    km = KMeans(n_clusters=tag1,random_state=0).fit(df)
    centroids = km.cluster_centers_
    # values = {i: df[np.where(km.labels_ == i)] for i in range(km.n_clusters)}
    # label_length = len(values)
    # length_value = []
    # for i in range(len(values)):
    #     length_value.append(len(values[i]))
    mem1=[]
    dist_list = []  # for calculating distance
    for i in range(0, len(centroids)):
        for j in range(0, len(centroids)):
            x1 = centroids[i][0]
            x2 = centroids[j][0]
            y1 = centroids[i][1]
            y2 = centroids[j][1]
            temp = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
            dist = math.sqrt(temp)

            # dist_list.append(list(zip(centroids[i][:], centroids[j][:], itertools.repeat(dist))))
            
            memdict=dict()
            memdict={'x1':x1,'y1':y1,'x2':x2,'y2':y2,'dist':dist}
            mem1.append(memdict)
    print(mem1)
        
        
        
# dist_len = len(dist_list)
# e = time.time()
# t = e-s
    #     print(dist_list)
    #     print(t)

    # print(centroids)
    
    


    return render_template("display.html", rows=mem1)
    
        # return render_template("display.html", centroid=centroids, distances = dist_list, timey=t, length=dist_len, length_value=length_value, values=values, label_length=label_length)

    
    
# plt.scatter(df['x'], df['y'], c= km.labels_.astype(float), s=50, alpha=0.5)
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
# plt.show()

        
port = int(os.getenv("PORT", 5000))
if __name__ == '__main__':
 application.run(port=port,debug=True)   
        









      

      
      
    




