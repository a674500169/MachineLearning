# -*- encoding: utf-8 -*-
"""
@File    :   hbase.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:25   chen.yi      1.0         None
"""
import happybase

class hbaseUtil():
    def __init__(self, address, port):
        self.conn = happybase.Connection(
            host = address
            , port = int(port)
        )

    def insetRowkey(self,table_name,rowkey,data):
        t = self.conn.table(table_name)
        t.put(rowkey, data=data)

    def getRowkey(self,table_name,rowkey):
        print(table_name)
        t = self.conn.table(table_name)
        return t.row(rowkey)

    def delRowkey(self,table_name,rowkey,column_name=None):
        t = self.conn.table(table_name)
        t.delete(rowkey,columns=column_name)