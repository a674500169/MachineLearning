# -*- encoding: utf-8 -*-
"""
@File    :   redis.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:24   chen.yi      1.0         None
"""
import redis
import logging

class redisUtil():
    def __init__(self, address, port, password, db):
        self.conn = redis.ConnectionPool(
            host = address,
            port = port,
            password = password,
            db = db
        )
        self.redis = redis.StrictRedis(connection_pool=self.conn)

    def hmset(self, key, contentJson):

        result = self.redis.hmset(key, contentJson)
        if result:
            logging.info("redis inset succsess")
        else:
            logging.info("redis inset error")

    def set(self, key, contentJson):

        result = self.redis.set(key, contentJson)
        if result:
            logging.info("redis inset succsess")
        else:
            logging.info("redis inset error")