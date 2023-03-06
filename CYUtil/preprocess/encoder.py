# -*- encoding: utf-8 -*-
"""
@File    :   encoder.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:33   chen.yi      1.0         None
"""
import numpy as np
from sklearn.preprocessing import LabelEncoder

"""
hash特征编码 
乘法哈希，
"""
class HashEncode():
    def __init__(self):
        self.config = {"mul": self._bernstein}

    def _bernstein(self, key,seed=31):
        """
        乘法哈希编码
        :param key: 编码字符串 string
        :param seed: 编码种子 int st.31, 131, 1313, 13131, 131313
        :return: 哈希编码 int
        """
        _hash = 0
        for s in key:
            _hash = seed*_hash + ord(s)
        return _hash

    def hash_id(self, id_str, nuniqs, times=3, strategy="mul"):
        """
        哈希主函数
        :param str: 编码字符串 string
        :param times: 哈希空间倍数 int
        :param strategy: 哈希算法 sting
        :return: 哈希值
        """
        hash_fn = self.config[strategy]
        return hash_fn(str(id_str)) % (nuniqs * times)

"""
label特征编码 
未知类型调整为 Unknown
"""
class LabelEncoderExt(object):
    def __init__(self):
        """
        It differs from LabelEncoder by handling new classes and providing a value for it [Unknown]
        Unknown will be added in fit and transform will take care of new item. It gives unknown class id
        """
        self.label_encoder = LabelEncoder()
        # self.classes_ = self.label_encoder.classes_

    def fit(self, data_list):
        """
        This will fit the encoder for all the unique values and introduce unknown value
        :param data_list: A list of string
        :return: self
        """
        self.label_encoder = self.label_encoder.fit(list(data_list) + ['Unknown'])
        self.classes_ = self.label_encoder.classes_

        return self

    def fit_transform(self, data_list):
        self.label_encoder = self.label_encoder.fit(list(data_list) + ['Unknown'])
        self.classes_ = self.label_encoder.classes_
        return self.label_encoder.transform(data_list)

    def transform(self, data_list):
        return self.label_encoder.transform(data_list)

    def transform_fill(self, data_list):
        """
        This will transform the data_list to id list where the new values get assigned to Unknown class
        :param data_list:
        :return:
        """
        new_data_list = np.array(data_list)
        unknown_arr = set(data_list) - set(self.label_encoder.classes_)
        new_data_list = np.where(np.in1d(new_data_list[:], list(unknown_arr)), "Unknown", new_data_list)
        #         print(np.where(np.in1d(new_data_list[:], list(unknown_arr)), "Unknown", new_data_list))
        #         print(set(self.label_encoder.classes_))
        #         print(set(data_list) - set(self.label_encoder.classes_))
        #         for unique_item in np.unique(data_list):
        #             if unique_item not in self.label_encoder.classes_:
        #                 new_data_list = ['Unknown' if x==unique_item else x for x in new_data_list]

        return self.label_encoder.transform(new_data_list)