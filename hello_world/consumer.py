#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika

# 认证
credentials = pika.PlainCredentials("guest", "guest")

# 连接参数
conn_params = pika.ConnectionParameters("58.87.84.167", credentials=credentials)

# 创建连接
conn_broker = pika.BlockingConnection(conn_params)

# 获取channel
channel = conn_broker.channel()

# 声明交换器
channel.exchange_declare(exchange="hello-exchange", exchange_type="direct", passive=False, durable=False,
                         auto_delete=False)

# 声明队列
channel.queue_declare(queue="hello-queue")

# 绑定
channel.queue_bind(queue="hello-queue", exchange="hello-exchange", routing_key="hola")


# 创建consumer
def message_consumer(channel, method, header, body):
    channel.basic_ack(delivery_tag=method.delivery_tag)
    if body == "quit":
        channel.basic_cancel(consumer_tag="hello-consumer")
        channel.stop_consuming()
    else:
        print(body)
    return


# 订阅消费者
channel.basic_consume(message_consumer, queue="hello-queue", consumer_tag="hello-consumer")

# 开始消费
channel.start_consuming()
