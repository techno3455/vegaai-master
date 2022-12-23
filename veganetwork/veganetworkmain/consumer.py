'''import pika
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "veganetworkmain.settings")


params = pika.URLParameters('amqps://mxerukoj:vFAH8jBKvu2uYJ2N4vl5nCn4Hoy6qtM3@shark.rmq.cloudamqp.com/mxerukoj')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='veganetworkmain')


def callback(ch, method, properties, body):
    print('Received in vegatest')
    print(body)


channel.basic_consume(queue='veganetworkmain', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()'''
