# 项目简介
  为了提高日常工作中的研发效率，对常用的一些模型、方法进行封装使用。
  - 模型方面包含多个领域（CV、NLP、推荐系统、机器学习）模型，持续更新..。
  - 模块方面预计增加数据分析、特征处理、模型训练、数据库（redis、hive、hbase）连接等模块，持续更新..。

# 目录结构
```
CYUtil  
|── data
    |—— hbase.py
    |—— hive.py
    |—— impala.py
    |—— redis.py
│—— model
|   |—— cv
|   |—— ml
|   |—— nlp
|   |—— rs
|       |—— DeepFM.py
|── preprocess
    |—— common.py
    |—— encoder.py
    |—— math.py
|── train
    |—— metric.py
```

# 环境依赖&安装指南
1. sklearn
2. pytorch
3. numpy
4. pandas
5. jieba

```
pip install git+https://github.com/a674500169/MachineLearning.git@main
```

# 使用范例

```
from CYUtil.preprocess import hash_id
from CYUtil.model import DeepFM

train[k].map(lambda x: hash_id(x, v[0],v[1]))
model = DeepFM(cate_fea_nuniqs)

```

# 内容更新

#### v1.0.0:
    1. 增加推荐模型 DeepFM
    2. 特征预处理
    3. 数据库工具
    4. 模型评估指标


