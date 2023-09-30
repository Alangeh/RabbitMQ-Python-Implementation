import pika
import time
import random

#define connection parameters, localhost for local and server name if running on remote server
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

#create a new channel, default channel
channel = connection.channel()

#declare a queue
channel.queue_declare(queue='letterbox')

#publish queue to default exchange

messageId = 1

while(True):
    message = f"Testing RabbitMQ using Python. MessageId: {messageId}"
    
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)

    print(f"sent messgae: {message}")

    time.sleep(random.randint(1,4))

    messageId+=1


