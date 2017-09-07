#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: yuanhao<48194274@qq.com>
@see:
"""

import time
from automatic_task import app

@app.task()
def run(x,y):
    time.sleep(5)
    return x+y
