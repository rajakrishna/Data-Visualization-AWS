"""Cloud Foundry test"""
from flask import Flask,render_template,request
import os
import pyodbc
import csv

app = Flask(__name__)



@app.route('/')
def home():
  return render_template("home.html")

@app.route('/showdb5', methods=['GET', 'POST'])
def showdb5():
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = cnxn.cursor()
    cursor.execute("SELECT StateName from voting where TotalPop between 5000 and 10000 ")
    row = cursor.fetchall()
    return render_template("showdb.html", row=row)

@app.route('/showdb10', methods=['GET', 'POST'])
def showdb10():
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = cnxn.cursor()
    cursor.execute("SELECT StateName from voting where TotalPop between 10000 and 50000 ")
    row = cursor.fetchall()
    return render_template("showdb.html", row=row)



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


@app.route('/piechart', methods=['GET', 'POST'])
def piechart():
    nvalue = int(request.form['nvalue'])
    con = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:hello1997.database.windows.net,1433;Database=quakes;Uid=raja@hello1997;Pwd={azure@123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    # a=nvalue #chnage this variable
    start=nvalue+990 #10
    end=17000
    age_interval=[0]
    val=start
    while val<end:
        val+=start
        age_interval.append(val)
    mem=[]
    for i in range(0,len(age_interval)-1):
        #query="select (count(*)) as count from voting where age > "+str(age_interval[i])+" and age<"+str(age_interval[i+1])
        query="select count(*) as count from voting where Registered >"+str(age_interval[i])+" and Registered< "+str(age_interval[i+1])
        cur=con.cursor()
        cur.execute(query)
        result=list(cur.fetchall())
        vtt=str(age_interval[i])+"-"+str(age_interval[i+1])
        for row in result: 
            memdict=dict()
            for j,val in enumerate(row):
                memdict["vtt"]=vtt
                memdict["States"]=val
                mem.append(memdict)
            print(mem)

    return render_template('barchart.html',a=mem,chart="bar")

port = int(os.getenv("PORT", 5000))
if __name__ == '__main__':
    app.run(port=port,debug=True)
