import redis
import os

redis_client = redis.StrictRedis(
    host='redis.finvedic.in',
    port=6379,
    db=0
)


# Test the connection
try:
    redis_client.ping()
    print("Connected to Redis successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis.")

