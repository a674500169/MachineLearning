# -*- encoding: utf-8 -*-
"""
@File    :   setup.py.py   
@Contact :   y.chen@shunwang.com
@License :   (C)Copyright 2022-2023
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/10 10:52   chen.yi      1.0         None
"""


from setuptools import setup, find_packages

setup(
    name="cy_package",
    version="0.0.1",
    keywords=("pip", "license", "licensetool", "tool", "gm"),
    description="the machine learning tools of y.chen.",
    # long_description="long_description",
    license="MIT Licence",

    url="https://github.com/a674500169/MachineLearning",
    author="y.chen",
    author_email="674500169@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['chardet']
)