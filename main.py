import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                               8080,
                                                               '/',
                                                               credentials))

channel = connection.channel()
for number in range(15):  # type: int
    channel.basic_publish(exchange='', routing_key='my_queue', body="Message"+str(number))

connection.close()MacBook-Pro-Ivan:pythonProject2 ivanzamyatin$ 
