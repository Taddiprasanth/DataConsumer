#test.py
import redis

r = redis.StrictRedis(
    host='redis.finvedic.in',
    port=6379,
    db=0
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
