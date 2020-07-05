from elasticsearch import Elasticsearch
import pyodbc 

sql_text = "select * from [NORTHWND].[dbo].[Orders]"
index_name = "hakan"

def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Elasticsearch Connected')
    else:
        print('Awww it could not connect!')
    return _es
es = connect_elasticsearch()

def create_index(index_name):
    if not es.indices.exists(index_name):
        es.indices.create(index=index_name)
        print(index_name+" indexi created")
    else:
        print(index_name+" already exist")
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

    
