##装饰器

###所有的函数可以方便的加上一段和该类函数有关但不用每次都添加的方法

```
def test(level):
    def log(func):
        def wrapper(*args):
            print 'cccc'
            return func(*args)
        return wrapper
    return log 

@test(level='yyy')
def aa(ee=2222):
    print 1111
aa()
```


##celery 分布式调度模块，将代码导入后，通过其他代码直接调用该模块

###调用方式


通过在python代码中增加模块并运行的方式执行

运行的方式：python->cerley->redis->执行代码


```
from glanceTasks import run
run.delay()

```


## 监控系统


### 数据采集

#### 采集部分


+ 信息采集
 
    - 服务器信息

    从glances获取系统信息，保存入mongodb


    - 自定义采集
    
    从任意的采集点（自定义url）对应采集数据

    - 数据保存

    存入mongodb中，不同的信息保存不同的库，mongodb做分片


+ 数据存储
    
    - 存储配置

    选择不同的数据驱动，目前存在mongdb中，mongodb做分片，不同的数据库存不同的内容

    - 写入

    - 读取

    - 状态


+ 数据处理
    
    - 触发条件设置

    - 计算处理


#### 任务调度
   
+ 查询任务
    - celery.app.control.Inspect

+ 更改任务

+ 定时任务

+ 处理反馈


#### 开发工具

sublime text 3 http://blog.csdn.net/mx472756841/article/details/50535517
