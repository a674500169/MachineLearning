# -*- encoding: utf-8 -*-
"""
@File    :   hive.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:25   chen.yi      1.0         None
"""

# def getDataByImpyla(sqlStr):
#     conn = connect(host='192.168.89.2', port=21050, user='yi.chen', password='yi@kktv')
#     cursor = conn.cursor()
#     cursor.execute(sqlStr)
#
#     if cursor.description != None:
#         col = [tuple_[0]for tuple_ in cursor.description]
#         datas = cursor.fetchall()
#         return pd.DataFrame(datas,columns=col)