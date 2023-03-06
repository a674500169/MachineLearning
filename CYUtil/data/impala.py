# -*- encoding: utf-8 -*-
"""
@File    :   impala.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:24   chen.yi      1.0         None
"""
import pandas as pd
import subprocess
from impala.dbapi import connect

class impalaUtil():
    def __init__(self, address, port, user, password):
        self.conn = connect(host = address, port=port, user=user, password=password)
        self.cursor = self.conn.cursor()

    def getDataByImpyla(self,sqlStr):
        self.cursor.execute(sqlStr)
        if self.cursor.description != None:
            col = [tuple_[0]for tuple_ in self.cursor.description]
            datas = self.cursor.fetchall()
            return pd.DataFrame(datas,columns=col)

def updata_hive(file_name,db_tb,dt_str):

    # tmp.db_tb
    # create table tmp.newusers_actor_ranking like superset_kk.newusers_actor_ranking; --split ',' -- no par
    # superset_kk.newusers_actor_ranking re create   --split '\t'
    # load data local inpath '%s' overwrite into table tmp.newusers_actor_ranking partition(dt=='%s');
    # insert overwrite table superset_kk.newusers_actor_ranking partition(dt='%s') select * from tmp.newusers_actor_ranking;

    hql = "load data local inpath '%s' overwrite into table %s partition(dt='%s')" % (
        file_name, db_tb, dt_str)
    # print(hql)
    load_cmd = '''hive -e "%s" && impala-shell -q "refresh %s" ''' % (hql, db_tb)
    status, output = subprocess.getstatusoutput(load_cmd)
    # print(output)
    if status !=0:
        print("load 失败")
        # exit(-1)
    else:
        print('hive插入成功')