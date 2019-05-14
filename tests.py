#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import docker
import requests

client = docker.from_env()


# Testing Symfony build

time.sleep(20)  # we expect all containers are up and running in 20 secs
for c in client.containers.list():
    print(c.name)
    print(c.status)

# Symfony PHP
php = client.containers.get('php')
php_log = php.logs()
print(php_log.decode())
assert php.status == 'running'
php_conf = php.exec_run("php-fpm -t")
assert 'configuration file /usr/local/etc/php-fpm.conf test is successful' in php_conf.output.decode()
php_proc = php.exec_run("ps aux |grep php-fpm")
assert 'php-fpm: master process (/usr/local/etc/php-fpm.conf)' in php_proc.output.decode()
assert 'fpm is running, pid' in php.logs()

mysql = client.containers.get('db')

assert mysql.status == 'running'
mycnf = mysql.exec_run("/usr/sbin/mysqld —verbose —help")
assert '' in mysql.output.decode()
mysql_log = mysql.logs()
print(mysql_log.decode())
assert "Ready to accept connections" in mysql_log.decode()

#response = requests.get("http://127.0.0.1:9000")
#assert response.status_code == 200
