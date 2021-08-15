#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
    print(f'Message: {body}')
    print(f'Method: {method}')

def receive_message():
    for i in range(0,5):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit'))
            channel = connection.channel()
        except Exception as e:
            print(e)
            print('Receiver is still waiting for the rabbit...')
            time.sleep(5)

    channel.queue_declare(queue='my-first-queue')
    channel.basic_consume(queue='my-first-queue', auto_ack=True, on_message_callback=callback)
    
    try:
        channel.start_consuming()
    except:
        connection.close()

def main():
    receive_message()

if __name__ == '__main__':
    main()
