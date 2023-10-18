import pika
from pika.exchange_type import ExchangeType

def alt_ex_on_message_received(ch, method, properties, body):
    print(f'alt exchange received message: {body}')

def main_ex_on_message_received(ch, method, properties, body):
    print(f'main exchange received message: {body}')

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='altExchange', exchange_type=ExchangeType.fanout)

channel.exchange_declare(
    exchange='mainexchange',
    exchange_type=ExchangeType.direct,
    arguments={'alternate-exchange': 'altExchange'}
)

channel.queue_declare(queue='altexchangequeue')

channel.queue_bind('altexchangequeue', 'altExchange')

channel.basic_consume(queue='altexchangequeue', auto_ack=True, on_message_callback=alt_ex_on_message_received)

channel.queue_declare(queue='mainexchangequeue')

channel.queue_bind('mainexchangequeue', 'mainexchange', 'test')

channel.basic_consume(queue='mainexchangequeue', auto_ack=True, on_message_callback=main_ex_on_message_received)

print('Starting consuming')