#!/usr/bin/env python

from elasticsearch import Elasticsearch

def create_index(es, index_name):
    print(f'Creating index {index_name}')
    es.indices.create(index=index_name, ignore=400)   

def insert_data(es, index_name, data):
    print(f'Adding data for user {data["name"]}')
    es.index(index=index_name, body=data)
    #es.index(index=index_name, id=10, body=data)

def main():
    es = Elasticsearch(host='172.20.0.4', port='9200', ssl_show_warn=False)

    index_name = 'test-from-python'

    person1 = {
            'name': 'Piotr',
            'age': '32',
            }

    person2 = {
            'name': 'Monika',
            'age': '29',
            }

    create_index(es, index_name)
    insert_data(es, index_name, person1)
    insert_data(es, index_name, person2)

if __name__ == '__main__':
    main()
