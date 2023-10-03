import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.fanout)
channel.exchange_declare(exchange='topicexchange', exchange_type=ExchangeType.fanout)

#message = "Routing implementation. Routed Message"
#channel.basic_publish(exchange='routing', routing_key='analyticsonly', body=message)
#channel.basic_publish(exchange='routing', routing_key='both', body=message)

user_payment_message = "Payment message for user routing"

channel.basic_publish(exchange='topicexchange', routing_key='user.europe.payments', body=user_payment_message) #key expects all consumers to receive message

print(f"Message sent: {user_payment_message}")

business_message = "Business message for Europe"

channel.basic_publish(exchange='topicexchange', routing_key='buiness.europe.order', body=business_message) #key expects only analytics consumer to receive messge

print(f"Message sent: {business_message}")

connection.close()