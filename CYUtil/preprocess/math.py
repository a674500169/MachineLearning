# -*- encoding: utf-8 -*-
"""
@File    :   math.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:32   chen.yi      1.0         None
"""
import numpy as np

"""
威尔逊修正 
未知类型调整为 Unknown
"""
def walson_ctr(score, count):
    n = count
    if n == 0: return 0
    z = 1.96 #1.96 -> 95% confidence
    phat = score
    denorm = 1. + (z*z/n)
    enum1 = phat + z*z/(2*n)
    enum2 = z * np.sqrt(phat*(1-phat)/n + z*z/(4*n*n))
    return (enum1-enum2)/denorm