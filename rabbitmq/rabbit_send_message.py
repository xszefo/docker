#!/usr/bin/env python

import pika
import time
import random

def send_message(message):
    for i in range(0,5):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
            channel = connection.channel()
        except Exception as e:
            print(e)
            print('Sender is still waiting for the rabbit...')
            time.sleep(5)

    channel.queue_declare(queue='my-first-queue')

    channel.basic_publish(exchange='', routing_key='my-first-queue', body=message)
    print(f'Sent message: {message}')

    connection.close()

def main():
    message = ''.join([str(random.randint(0,5)) for i in range(0,9)])
    send_message(message)

if __name__ == '__main__':
    main()
