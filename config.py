import redis
import os

redis_client = redis.StrictRedis(
    host='redis-18698.c280.us-central1-2.gce.redns.redis-cloud.com',
    port=18698,
    username="default",
    password="BKYiUHXCZv5rL1hI78j5Ph92kog2ZU6g",
    db=0
)


# Test the connection
try:
    redis_client.ping()
    print("Connected to Redis successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis.")

