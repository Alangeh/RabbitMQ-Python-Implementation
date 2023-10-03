import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.fanout)

message = "Hello, routing implementation. Routed Message"

channel.basic_publish(exchange='pubsub', routing_key='analyticsonly', body=message)

print(f"Message sent: {message}")

connection.close()