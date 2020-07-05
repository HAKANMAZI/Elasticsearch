from elasticsearch import Elasticsearch
import pyodbc 

sql_text = '''select [EmployeeID]
      ,[LastName]
      ,[FirstName]
      ,[Title]
      ,[TitleOfCourtesy]
      ,[BirthDate]
      ,[HireDate]
      ,[Address]
      ,[City]
      ,[Region]
      ,[PostalCode]
      ,[Country]
      ,[HomePhone]
      ,[Extension]
      --,[Photo]
      ,[Notes]
      ,[ReportsTo]
      ,[PhotoPath] from [NORTHWND].[dbo].[Employees]'''
      
index_name = "nag"

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Elasticsearch Connected')
    else:
        print('it could not connect!')
    return _es
es = connect_elasticsearch()

def create_index(index_name):
    if not es.indices.exists(index_name):
        es.indices.create(index=index_name)
        print(index_name+" index created")
    else:
        print(index_name+" index already exist")
    return index_name
index_name = create_index(index_name)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BDR59P4;'
                      'Database=NORTHWND;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()   
cursor.execute(sql_text)
columns = [column[0] for column in cursor.description]

for i,row in enumerate(cursor):
    rest = {column:row[i] for i,column in enumerate(columns)}
    
    es.index(index=index_name,id=i,body=rest)

def match():
    cursor.execute("select @@rowcount")
    rowcount = cursor.fetchall()[0][0]
    print('Mssql count: ', rowcount)
    res= es.search(index=index_name,body={'query':{'match_all':{}}})
    print('Elasticsearch count: ', res['hits']['total']['value'])   
    
match()
