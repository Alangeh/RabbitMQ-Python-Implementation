import pika
from pika.exchange_type import ExchangeType

def on_message1_received(ch, method, properties, body):
    print(f"Queue 1 new message: {body}")

def on_message2_received(ch, method, properties, body):
    print(f"Queue 2 new message: {body}")

#define connection parameters, localhost for local and server name if running on remote server
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

#create a new channel, default channel
channel = connection.channel()

channel.exchange_declare("simplehashing", "x-consisten-hash")

#declare a queue
channel.queue_declare(queue='letterbox1')

channel.queue_bind('letterbox1', 'simplehashing', routing_key='1')

channel.basic_consume(queue='letterbox1', auto_ack=True, on_message_callback=on_message1_received)


channel.queue_declare(queue='letterbox2')

channel.queue_bind('letterbox2', 'simplehashing', routing_key='4')

channel.basic_consume(queue='letterbox2', auto_ack=True, on_message_callback=on_message2_received)

print("Starting Consuming")

channel.start_consuming()