#!/usr/bin/env python

from elasticsearch import Elasticsearch

def main():
    es = Elasticsearch(
        ['172.19.0.4'],
        sniff_on_start=True,
        sniff_on_connection_fail=True,
        sniffer_timeout=60
    )

    for node in es.nodes.info()['nodes'].values():
        print(f'{node["name"]} - {node["host"]} - version {node["version"]}')
        print(f'Roles: {", ".join(node["roles"])}')
        print(10*'*')

if __name__ == '__main__':
    main()
