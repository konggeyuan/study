/home/webserver/mysql5.7/data
/home/www/


mkdir -pv /data/mysql


1������mysql�������ͨ��dockerfile�ļ����ɡ�
docker pull mysql:5.7

2������һ��������--rm�Ǹ���Dockerһ�����еĽ����˳���ɾ��������--name��������������Ϊmysql��-it�ǽ��뽻��ģʽ��-v�ǹ���sql����Ŀ¼��-e������root���룬-d�Ǻ�̨����
docker run --rm --name mysql -it -v /data/mysql/:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456  mysql:5.7.17 /bin/bash

3�������������my.cnf����������
cp /etc/mysql/my.cnf /var/lib/mysql

4���˳�����
exit


5. docker run -d -e MYSQL_ROOT_PASSWORD=admin --name mysql -v /data/mysql/my.cnf:/etc/mysql/my.cnf -v /data/mysql/data:/var/lib/mysql  -p 3306:3306 mysql:5.7

mysql -uroot -p -h docker��ip



