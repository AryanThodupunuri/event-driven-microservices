import pika, json, os, django

from products.models import product
from config import rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_password

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

params = pika.URLParameters(f'amqp://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_host}:{rabbitmq_port}')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print ('Reveived in admin')
    id = json.loads(body)
    print (id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print ('product likes increased !')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print ('Started Cosuming')

channel.start_consuming()

channel.close()