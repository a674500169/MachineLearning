# -*- encoding: utf-8 -*-
"""
@File    :   FM.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:39   chen.yi      1.0         None
"""

# import numpy as np
# import tensorflow as tf
# from tensorflow.keras import layers
# from tensorflow.keras import Model
#
#
# class FM(Model):
#     def __init__(self, feat_max, hide_size, output_size):
#         super(FM, self).__init__()
#
#         self.feat_field_size = sum(feat_max) + 1  # 特征领域长度
#         self.feat_size = len(feat_max)  # 特征长度
#         self.hide_size = hide_size  # 隐藏层size
#         self.output_size = output_size  # 目标size
#
#         self.feat_offset = np.array((0, *np.cumsum(feat_max)[:-1]), dtype=np.long)  # 特征索引汇总
#
#     def build(self, input_shape):
#         self.bias = []
#         self.w = []
#         for i in range(self.output_size):
#             self.bias.append(
#                 self.add_weight(
#                     name='bias_' + str(i),
#                     shape=(1,),
#                     initializer=tf.zeros_initializer(),
#                     trainable=True
#                 )
#             )
#
#             self.w.append(
#                 self.add_weight(
#                     name='w_' + str(i),
#                     shape=(self.feat_field_size, 1),
#                     initializer=tf.random_normal_initializer(),
#                     trainable=True
#                 )
#             )
#
#         self.V = self.add_weight(
#             name='V',
#             shape=(self.feat_field_size, self.hide_size),
#             initializer=tf.random_normal_initializer(),
#             trainable=True
#         )
#
#     def call(self, inputs):
#
#         # 构建特征索引
#         X = inputs + self.feat_offset
#
#         # 线性层
#         liners = []
#         for i in range(self.output_size):
#             liners.append(self.bias[i] + tf.reduce_sum(tf.nn.embedding_lookup(self.w[i], X), axis=1))
#
#         # 交叉层
#         cross = tf.nn.embedding_lookup(self.V, X)
#         square_sum = tf.square(tf.reduce_sum(cross, axis=1, keepdims=True))
#         sum_squeare = tf.reduce_sum(tf.square(cross), axis=1, keepdims=True)
#
#         cross_res = 0.5 * tf.reduce_sum(square_sum - sum_squeare, axis=2, keepdims=False)
#
#         # 输出层
#         output = []
#         for line in liners:
#             output.append(tf.sigmoid(line + cross_res))
#
#         return output