
### 常规命令

```

 export C_FORCE_ROOT="true" && celery -A glanceTasks worker --autoreload --loglevel=info


celery multi stopwait wl -A glanceTasks -l info

celery -A glanceTasks multi start wl -l info

celery -A glanceTasks multi restart wl -l info

celery -A glanceTasks multi stop 10 -l info

celery status -A glanceTasks

celery inspect -A glanceTasks active --destination=yuanhao@mu77.com 启动选择某节点启动


celery -A proj control enable_events 查看活动信息


from automatic_task.module1 import run

├── __init__.py
├── module1
│   ├── task1.py
├── task3.py
├── taskconfig.py


```

### 网址

#### 中英文3.1文档

http://docs.celeryproject.org/en/3.1/index.html

http://docs.jinkan.org/docs/celery/index.html

#### 学习教程

##### 语言学习

https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000

##### celery 案例

http://www.cnblogs.com/chenice/p/6918435.html

http://blog.csdn.net/happyAnger6/article/details/51408266

https://segmentfault.com/a/1190000007780963

http://blog.csdn.net/happyanger6/article/details/51533321


##### Flask 教学

http://www.bjhee.com/flask-5.html

http://docs.jinkan.org/docs/flask/quickstart.html
