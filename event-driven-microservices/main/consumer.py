import pika

from main import Product, db
from config import rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_password

params = pika.URLParameters(f'amqp://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_host}:{rabbitmq_port}')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print ('Reveived in main')
    data = json.loads(body)
    print (body)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
    
    elif properties.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()

    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print ('Started Cosuming')

channel.start_consuming()

channel.close()