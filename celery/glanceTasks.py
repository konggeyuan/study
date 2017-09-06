#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
glance 任务队列
@version: 1.0
@author: yuanhao<48194274@qq.com>
@see:
"""

from celery import Celery
import gevent
import pymongo,sys,ast,requests,json,time
from urllib2 import urlopen

UNIX_TIMENOW = int(time.time());
timenow = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(UNIX_TIMENOW))
CTIME = time.mktime(time.strptime(timenow, '%Y-%m-%d %H:%M:%S'))

DB_HOST='localhost'
DB_PORT=27017


#本地的redis队列
REDIS_HOST='127.0.0.1'
REDIS_PORT='6379'


##
# @Synopsis  取glance主机信息
#
# @Param DB_HOST    主机信息
# @Param DB_PORT    主机端口
#
# @Returns   主机列表
def getGlanceHosts(DB_HOST,DB_PORT):
    
    #链接数据库
    conn = pymongo.MongoClient(host=DB_HOST, port=DB_PORT)
    gdb = conn.glances

    return gdb


##
# @Synopsis  主机获取数据,并写入mongdb
#
# @Param tservers 主机列表
#
# @Returns   
def getGlancesData(gdb):
    tservers = gdb.servers.find()
    ip=[]
    for server in tservers:
        url = 'http://'+server['ip']+":61208/api/2/all"
        r = requests.get(url)
        record = r.json()
        ip.append(gevent.spawn(postGlancesDataStore,record,gdb))
        gevent.joinall(ip)
        #postGlancesDataStore(record,gdb)
    return 


##
# @Synopsis  存储数据库
#
# @Param record glances服务器ip
#
# @Returns   
def postGlancesDataStore(record,gdb):
    serverSystem = record['system']
    cTime = time.mktime(time.strptime(record['now'], '%Y-%m-%d %H:%M:%S'))
    monitors = [
        'cpu', 'memswap', 'mem', 'diskio', 'network',
        'fs', 'processcount', 'ports', 'docker']
    for i in record:
       if i in monitors:
           if isinstance(record[i], dict):
               record[i]['ctime'] = cTime
               record[i]['hostname'] = serverSystem['hostname']
               record[i]['hr_name'] = serverSystem['hr_name']

               tb = 'gdb.'+i
               tb = eval(tb.encode('utf-8'))
               tb.insert(record[i])
                
           if isinstance(record[i], list):
               for l in record[i]:

                   # unicode转换

                   tmp = json.dumps(l)
                   tmp = json.loads(tmp)

                   tmp['ctime'] = cTime 
                   tmp['hostname'] = serverSystem['hostname']
                   tmp['hr_name'] = serverSystem['hr_name']
                   if len(tmp) != 0:
                       # print(mydb.i.insert(tmp))
                       tb = 'gdb.'+i
                       tb = eval(tb.encode('utf-8'))
                       tb.insert(tmp)

    return 

BORKER = 'redis://'+REDIS_HOST+':'+REDIS_PORT
app = Celery('glance_tasks',broker=BORKER)
@app.task()

##
# @Synopsis  任务程序
#
# @Returns   
def run():
    global CTIME,DB_HOST,DB_PORT,timenow
    hosts=getGlanceHosts(DB_HOST,DB_PORT)
    getGlancesData(hosts)
    #return timenow+'---------->'+' ok'

