import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='altExchange', exchange_type=ExchangeType.fanout)

channel.exchange_declare(
    exchange='mainexchange',
    exchange_type=ExchangeType.direct,
    arguments={'alternate-exchange': 'altExchange'}
)

message = 'hellow thsi is alternaate exchange example'

channel.basic_publish(exchange='mainexchange', routing_key='test', body=message)

print(f'sent message: {message}')

connection.close()