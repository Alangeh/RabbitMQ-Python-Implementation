import pika
from pika.exchange_type import ExchangeType

#define connection parameters, localhost for local and server name if running on remote server
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

#create a new channel, default channel
channel = connection.channel()

#declare exchanges
channel.exchange_declare("simplehashing", "x-consisten-hash")

routing_key = "Hash message"

message = "This is the hashing message"
#publish queue to default exchange
channel.basic_publish(exchange='headerexchange', 
                      routing_key=routing_key, 
                      body=message)

print(f"sent message: {message}")

connection.close()
