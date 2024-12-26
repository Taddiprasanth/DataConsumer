#test.py
import redis

r = redis.Redis(
    host='redis-18698.c280.us-central1-2.gce.redns.redis-cloud.com',
    port=18698,
    decode_responses=True,
    username="default",
    password="BKYiUHXCZv5rL1hI78j5Ph92kog2ZU6g",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
