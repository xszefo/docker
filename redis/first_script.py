#!/usr/bin/env python
import redis

client = redis.Redis(host='localhost', port=6379)

client.set('NAME', 'PIOTR')
client.set('SCORE', '10')

name = client.get('NAME').decode()
score = client.get('SCORE').decode()

print(name, score)
