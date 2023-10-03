import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, meethod, properties, body):
    print(f"Analytic Service - new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

################### direct exchange start ################

#channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

#queue = channel.queue_declare(queue='', exclusive=True)

#channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='analyticsonly')
#channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='both')

################### direct exchange end ##################


################### topic exchange start #################

channel.exchange_declare(exchange='topicexchange', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='topicexchange', queue=queue.method.queue, routing_key='*.europe.*') #the * reprents only one word before or after the word europe

################### topic exchange end ###################

channel.basic_consume(queue=queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

print("Starting consuming")

channel.start_consuming()