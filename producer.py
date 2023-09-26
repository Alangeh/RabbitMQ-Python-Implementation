import pika

#define connection parameters, localhost for local and server name if running on remote server
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

#create a new channel, default channel
channel = connection.channel()

#declare a queue
channel.queue_declare(queue='letterbox')

#publish queue to default exchange
message = "Testing RabbitMQ using Python"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"sent messgae: {message}")

connection.close()
