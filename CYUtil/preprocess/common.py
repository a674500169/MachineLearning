# -*- encoding: utf-8 -*-
"""
@File    :   common.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:33   chen.yi      1.0         None
"""
import numpy as np

"""
数据压缩 
未知类型调整为 Unknown
"""
def compressType(_df):
    colFloat64 = [_df.columns[i] for i, name in enumerate(_df.dtypes) if name == "float64"]
    colInt64 = [_df.columns[i] for i, name in enumerate(_df.dtypes) if name == "int64"]

    _df[colFloat64] = _df[colFloat64].astype(np.float32)
    _df[colInt64] = _df[colInt64].astype(np.int32)
    return _df