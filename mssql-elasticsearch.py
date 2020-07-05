from elasticsearch import Elasticsearch
import pyodbc 


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Elasticsearch Connected')
    else:
        print('Awww it could not connect!')
    return _es
es = connect_elasticsearch()

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BDR59P4;'
                      'Database=NORTHWND;'
                      'Trusted_Connection=yes;')

def send_data_to_elastic(CategoryID,CategoryName,Description,Picture):
    e1={
      "CategoryName":CategoryName
      ,"Description":Description
      ,"Picture":Picture
    }
    print(e1)
    es.index(index='hey1',doc_type='employee',id=CategoryID,body=e1)




cursor = conn.cursor()
cursor.execute("select *  FROM [NORTHWND].[dbo].[Categories]")

for row in cursor:
    send_data_to_elastic(row[0],row[1],row[2],str(row[3]))
    



         

    

    

    res= es.search(index='hey1',body={'query':{'match_all':{}}})
    print('Got hits:', res['hits']['total']['value'])
    print(res['hits']['hits'])
    print("-------------------------")
    
    res= es.search(index='hey1',body={'query':{'match':{'first_name':'nitin'}}})
    print(res['hits']['hits'])
    
    
    print("%%%%%%%   bool   %%%%%%%%")
    res= es.search(index='hey1',body={
            'query':{
                'bool':{
                    'must':[{
                            'match':{
                                'first_name':'nitin'
                            }
                        }]
                }
            }
        })
    print(res['hits']['hits'])
    
    print("%%%%%%%   filter   %%%%%%%%")
    res= es.search(index='hey1',body={
            'query':{
                'bool':{
                    'must':{
                        'match':{
                            'first_name':'nitin'
                        }
                    },
                    "filter":{
                        "range":{
                            "age":{
                                "gt":27
                            }
                        }
                    }
                }
            }
        })
    print(res['hits']['hits'])
    
    print("%%%%%%%   full text search   %%%%%%%%")
    res= es.search(index='hey1',doc_type='employee',body={
            'query':{
                'match':{
                    "about":"play cricket"
                }
            }
        })
    for hit in res['hits']['hits']:
        print(hit['_source']['about'])
        print(hit['_score'])
        print('**********************')