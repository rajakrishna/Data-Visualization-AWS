"""Cloud Foundry test"""
from flask import Flask,render_template,request
import os
import pyodbc
import csv

app = Flask(__name__)



@app.route('/')
def home():
#   return render_template("home.html")


# @app.route('/magsearch', methods=['GET', 'POST'])
# def magsearch():
#     mag1 = request.form['mag1']
#     mag2 = request.form['mag2']
#     con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     query="Select mag,latitude from quake3 where mag between '"+mag1+"' and '"+mag2+"'"
#     columns=['mag','latitude']
#     dic=dict()
#     cur=con.cursor()
#     mem=[]
#     cur.execute(query)
#     result=list(cur.fetchall())
#     for row in result:
#         memdict=dict()
#         for j,val in enumerate(row):
#             memdict[columns[j]]=val
#         mem.append(memdict)
#     # a=[1,2,3,4,5]
#     return render_template('chart.html',a=mem,chart="pie")

# @app.route('/magsearch', methods=['GET', 'POST'])
# def magsearch():
#     mag1 = request.form['mag1']
#     mag2 = request.form['mag2']
#     con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
#     query="Select mag,latitude from quake3 where mag between '"+mag1+"' and '"+mag2+"'"
#     columns=['mag','latitude']
#     dic=dict()
#     cur=con.cursor()
#     mem=[]
#     cur.execute(query)
#     result=list(cur.fetchall())
#     for row in result:
#         memdict=dict()
#         for j,val in enumerate(row):
#             memdict[columns[j]]=val
#         mem.append(memdict)
#     # a=[1,2,3,4,5]
#     return render_template('barchart.html',a=mem,chart="bar")
    con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    a=10
    start=0
    end=100
    age_interval=[0]
    val=start
    while val<end:
        val+=10
        age_interval.append(val)
    mem=[]
    for i in range(0,len(age_interval)-1):
        query="select (count(*))as count from titanic where age > "+str(age_interval[i])+" and age<"+str(age_interval[i+1])
        cur=con.cursor()
        cur.execute(query)
        result=list(cur.fetchall())
        
        age_group=str(age_interval[i])+"-"+str(age_interval[i+1])
        for row in result: 
            memdict=dict()
            for j,val in enumerate(row):
                memdict["age_group"]=age_group  
                memdict["count"]=val
                mem.append(memdict)
            print(mem)

    return render_template('barchart.html',a=mem,chart="bar")

port = int(os.getenv("PORT", 5000))
if __name__ == '__main__':
    app.run(port=port,debug=True)
