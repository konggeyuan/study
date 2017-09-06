
```

 export C_FORCE_ROOT="true" && celery -A glanceTasks worker --autoreload --loglevel=info


celery multi stopwait wl -A glanceTasks -l info

celery -A glanceTasks multi start wl -l info

celery -A glanceTasks multi restart wl -l info

celery -A glanceTasks multi stop 10 -l info

celery status -A glanceTasks

celery inspect -A glanceTasks active --destination=yuanhao@mu77.com 启动选择某节点启动


celery -A proj control enable_events 查看活动信息
```


