#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    Data_Analysis
#F-Name:    celery.py
#Login:     Administrator   
#Descripton:
#__Author__  Smartwy
#Date:      2020/5/22 14:48:09
#Version:

'''
    
'''

from celery import Celery
from django.conf import settings
import os

# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_email.settings')

# 创建应用
app = Celery("demo")
# 配置应用
app.conf.update(
    # 配置broker, 这里我们用redis作为broker
    broker_url='redis://127.0.0.1:6379/0',
    result_backend = 'redis://127.0.0.1:6379/1', # 结果存储，一定要写，不让报错
    # CELERY_RESULT_BACKEND = 'django-db', # 使用django的数据库 保存结果
)
# 设置app自动加载任务
# 从已经安装的app中查找任务
app.autodiscover_tasks(settings.INSTALLED_APPS)

