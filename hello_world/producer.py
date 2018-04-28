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
channel.exchange_declare(exchange="hello-exchange", exchange_type='direct', passive=False, durable=False, auto_delete=False)

# 获取消息
msg = 'Hello World 3'

# 设置消息参数
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

# 发送消息
channel.basic_publish(body=msg, exchange="hello-exchange", properties=msg_props, routing_key="hola")
