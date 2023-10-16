import pika
from pika.exchange_type import ExchangeType

#define connection parameters, localhost for local and server name if running on remote server
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

#create a new channel, default channel
channel = connection.channel()

#declare exchanges
channel.exchange_declare(exchange="headerexchange", exchange_type=ExchangeType.headers)

message = "This message will be sent with headers"

#publish queue to default exchange
channel.basic_publish(exchange='headerexchange', 
                      routing_key='', 
                      body=message,
                      properties=pika.BasicProperties(headers={"name": "lionel"}))

print(f"sent message: {message}")

connection.close()
