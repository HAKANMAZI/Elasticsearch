# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:20:31 2020

@author: HknMz
tips : https://medium.com/naukri-engineering/elasticsearch-tutorial-for-beginners-using-python-b9cb48edcedc
"""

from elasticsearch import Elasticsearch


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
        
    
def send_data_to_elastic():
    e1={
        "first_name":"nitin",
        "last_name":"panwar",
        "age": 27,
        "about": "Love to play cricket",
        "interests": ['sports','music'],
    }
    print(e1)
    es.index(index='hey1',doc_type='employee',id=3,body=e1)
    

def select_data_from_elastic(index='hey1',doc_type='employee',id=3):    
    res=es.get(index=index,doc_type=doc_type,id=id)
    print (res)

def delete_data_from_elastic(index='hey1',doc_type='employee',id=3):    
    res=es.delete(index=index,doc_type=doc_type,id=id)
    print (res)
    
def search():
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
