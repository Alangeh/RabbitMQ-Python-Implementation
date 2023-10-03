import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, meethod, properties, body):
    print(f"Analytic Service - new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='topicexchange', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='topicexchange', queue=queue.method.queue, routing_key='user.#') # the .# represents anything after the word 'user'

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print("Starting consuming")

channel.start_consuming()