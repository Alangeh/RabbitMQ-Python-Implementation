import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, meethod, properties, body):
    print(f"Payment Service - new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='paymentsonly')
channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='both')

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print("Starting consuming")

channel.start_consuming()