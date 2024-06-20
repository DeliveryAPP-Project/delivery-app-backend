import redis

redis_connection = redis.Redis(host="localhost", port=6379)


def set_redis_value(key, value):
    redis_connection.set(key, value)


def delete_redis_value(key):
    redis_connection.delete(key)


def get_redis_value(key):
    redis_connection.get(key)
