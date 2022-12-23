'''import pika, json

params = pika.URLParameters('amqps://wibhnkzk:X-Xfu_vMUOoeWNTFuOZBUkzFcq-eZuwl@baboon.rmq.cloudamqp.com/wibhnkzk')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='veganetworkscript', body=json.dumps(body), properties=properties)

#amqps://rviiesyu:UKg2Nq6IzI5-gD2vJcL36l-Mkp_DBgp9@shrimp.rmq.cloudamqp.com/rviiesyu

import pika

params = pika.URLParameters('amqps://rviiesyu:UKg2Nq6IzI5-gD2vJcL36l-Mkp_DBgp9@shrimp.rmq.cloudamqp.com/rviiesyu')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='veganetworkmain', body='Hola')'''
