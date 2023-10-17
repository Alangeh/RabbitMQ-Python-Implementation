import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"Received new message: {body}")

#define connection parameters, localhost for local and server name if running on remote server
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

#create a new channel, default channel
channel = connection.channel()

channel.exchange_declare(exchange="secondexchange", exchange_type=ExchangeType.fanout)

#declare a queue
channel.queue_declare(queue='letterbox')

channel.queue_bind('letterbox', 'secondexchange')

channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()