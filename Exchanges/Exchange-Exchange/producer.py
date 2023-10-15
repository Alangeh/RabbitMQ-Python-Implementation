import pika
from pika.exchange_type import ExchangeType

#define connection parameters, localhost for local and server name if running on remote server
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

#create a new channel, default channel
channel = connection.channel()

#declare exchanges
channel.exchange_declare(exchange="firstexchange", exchange_type=ExchangeType.direct)

channel.exchange_declare(exchange="secondexchange", exchange_type=ExchangeType.fanout)

#bind exchanges
channel.exchange_bind("secondexchange", "firstexchange")

message = "This message has gone through multiple exchanges"

#declare a queue
channel.queue_declare(queue='letterbox')

#publish queue to default exchange
channel.basic_publish(exchange='firstexchange', routing_key='', body=message)

print(f"sent message: {message}")

connection.close()
