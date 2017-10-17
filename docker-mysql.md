/home/webserver/mysql5.7/data
/home/www/


mkdir -pv /data/mysql


1、下载mysql镜像或者通过dockerfile文件生成。
docker pull mysql:5.7

2、启动一个容器，--rm是告诉Docker一旦运行的进程退出就删除容器，--name是设置容器名称为mysql，-it是进入交互模式，-v是挂载sql数据目录，-e是设置root密码，-d是后台运行
docker run --rm --name mysql -it -v /data/mysql/:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456  mysql:5.7.17 /bin/bash

3、拷贝容器里的my.cnf到宿主机里
cp /etc/mysql/my.cnf /var/lib/mysql

4、退出容器
exit


5. docker run -d -e MYSQL_ROOT_PASSWORD=admin --name mysql -v /data/mysql/my.cnf:/etc/mysql/my.cnf -v /data/mysql/data:/var/lib/mysql  -p 3306:3306 mysql:5.7

mysql -uroot -p -h docker的ip



