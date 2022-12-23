'''import pika
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veganetworkmain.settings")


params = pika.URLParameters('amqps://wibhnkzk:X-Xfu_vMUOoeWNTFuOZBUkzFcq-eZuwl@baboon.rmq.cloudamqp.com/wibhnkzk')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='veganetworkmain')


def callback(ch, method, properties, body):
    print('Received in vegatest')
    print(body)


channel.basic_consume(queue='veganetworkmain', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

import pika

params = pika.URLParameters('amqps://rviiesyu:UKg2Nq6IzI5-gD2vJcL36l-Mkp_DBgp9@shrimp.rmq.cloudamqp.com/rviiesyu')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='veganetworkmain')

def callback(ch, method, properties, body):
    print('Received in veganetworkmain')
    print(body)

channel.basic_consume(queue='veganetworkmain', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()'''