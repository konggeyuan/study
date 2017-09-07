#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: yuanhao<48194274@qq.com>
@see:
"""
from celery import Celery

app = Celery('demo')
app.config_from_object('automatic_task.taskconfig')
