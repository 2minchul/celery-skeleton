# coding=utf-8

from constant import *

broker_url = get_rabbitmq_uri('localhost')
# Or use Redis
# broker_url = get_redis_uri('localhost', 0)

result_backend = 'db+' + get_mysql_uri('localhost', db='celery')
# Or use Redis
# result_backend = 'db+' + get_redis_uri('localhost', 1)
