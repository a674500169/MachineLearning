# -*- encoding: utf-8 -*-
"""
@File    :   hash_trick.py
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/10 11:12   chen.yi      1.0         None
"""



def _bernstein(key,seed=31):
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

config = {"mul": _bernstein}

def hash(id_str, nuniqs,times=3, strategy="mul"):
    """
    哈希主函数
    :param str: 编码字符串 string
    :param times: 哈希空间倍数 int
    :param strategy: 哈希算法 sting
    :return: 哈希值
    """
    config = {"mul":_bernstein}
    hash_fn = config[strategy]
    return hash_fn(str(id_str)) % (nuniqs * times)





