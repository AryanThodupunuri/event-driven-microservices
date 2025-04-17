import pika, json

from config import rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_password

params = pika.URLParameters(f'amqp://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_host}:{rabbitmq_port}')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)