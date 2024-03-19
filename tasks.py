# tasks.py
from huey import RedisHuey
from contextlib import contextmanager
import pickle


huey = RedisHuey(url='redis://redis-service:6379')

@huey.task()
def store_data(key, value):
    # with redis_connection() as r:
    #     # Set key-value pair in Redis
    #     r.redis.set(key, value)
    #     # Optionally, you can also set an expiry time for the key
    #     # r.expire(key, <expiry-time-in-seconds>)
    global huey
    result = huey.put(key, value)
    return result

def get_data(key):
    # with redis_connection() as r:
    #     value = r.redis.get(key)
    global huey
    ans= huey.get_raw(key, True)
    data = pickle.loads(ans)
    print('phani')
    print(str(data))
    return str(data)
