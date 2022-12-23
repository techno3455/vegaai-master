'''import pika, json

params = pika.URLParameters('amqps://nbarpfhd:S3Hb7VdpMOLAtU3SNy3jnap-Cl2X-9fR@toad.rmq.cloudamqp.com/nbarpfhd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='veganetworkscript', body=json.dumps(body), properties=properties)'''
