# -*- encoding: utf-8 -*-
"""
@File    :   metric.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/6 9:36   chen.yi      1.0         None
"""
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score


class AUCMetric():
    def __init__(self, model, df, input_feat):
        self.model = model
        self.df = df
        self.input_feat = input_feat

    def get_global_auc(self, label):
        y_pred_prob = self.model.predict(self.df[self.input_feat], num_iteration=self.model.best_iteration)
        # 评估模型 AUC
        return roc_auc_score(self.df[label], y_pred_prob)

    def get_avg_gauc(self, g_feat, g_label, is_tf_model=False, index=0, target_num=1):

        self.g_label = g_label
        temp_df = self.df[[g_feat, self.g_label]].groupby(g_feat).progress_apply(self.threw_inval_users).reset_index()

        """ 剔除 全正样本或负样本的用户 """
        label_users = temp_df[(temp_df[self.g_label] >= 1) & (temp_df[self.g_label] != temp_df["count"])][g_feat].values

        fitlered_df = self.df[self.df[g_feat].isin(label_users)]

        """ 开始计算 """
        if is_tf_model:
            preds = self.model.predict(fitlered_df[self.input_feat])
            y_pred_prob = preds[index].reshape(-1)
        else:
            y_pred_prob = self.model.predict(fitlered_df[self.input_feat], num_iteration=self.model.best_iteration)
        labels = fitlered_df[self.g_label].values
        ss = fitlered_df.groupby("user_id")[self.g_label].sum()

        user_id_list = fitlered_df[g_feat].values
        return self.avg_group_auc(labels, y_pred_prob, user_id_list)

    def avg_group_auc(self, labels, preds, user_id_list):
        """Calculate group auc"""
        df = pd.DataFrame({"user_id": user_id_list.tolist(), "labels": labels.tolist(), "preds": preds.tolist()})
        users_auc = df.groupby("user_id").apply(lambda x: roc_auc_score(x["labels"], x["preds"]))
        return users_auc.mean()

    def threw_inval_users(self, g_df):
        count = g_df.shape[0]
        label = g_df[g_df[self.g_label] == 1].shape[0]
        return pd.DataFrame(np.array([[count, label]]), columns=['count', self.g_label])