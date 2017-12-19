# coding=utf-8
def get_rabbitmq_uri(host, user='username', pw='password', vhost='/'):
    from urllib.parse import quote
    return 'amqp://{0}:{1}@{2}:5672/{3}'.format(user, pw, host, quote(vhost, safe=''))


def get_mysql_uri(host, user='root', pw='password', db=''):
    return 'mysql://{}:{}@{}/{}'.format(user, pw, host, db)


def get_redis_uri(host, db_num=0, pw=None):
    if isinstance(pw, str):
        pw = pw + '@'
    else:
        pw = ''

    return 'redis://:{}{}:6379/{}'.format(pw, host, db_num)
