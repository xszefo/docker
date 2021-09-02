#!/usr/bin/env python

from elasticsearch import Elasticsearch

def main():
    es = Elasticsearch(
        ['172.19.0.4'],
        sniff_on_start=True,
        sniff_on_connection_fail=True,
        sniffer_timeout=60
    )

    cluster_health = es.cluster.health()

    print(f'Cluster name: {cluster_health["cluster_name"]}')
    print(f'Health: {cluster_health["status"]}')
    print(f'Number of nodes: {cluster_health["number_of_nodes"]}')

if __name__ == '__main__':
    main()
