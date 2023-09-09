import redis
from requests import Session

session = Session()

redis_connection = redis.Redis(host='redis', port=6379, db=1)


def save_user_session_key(user_id, session_key):
    """Save user_id and session_key in Redis storage."""
    transaction = redis_connection.pipeline()
    transaction.delete(user_id)
    transaction.set(user_id, session_key)
    transaction.execute()


def get_user_session_key(user_id):
    """Retrieve session_key based on user_id from Redis storage."""
    session_key = redis_connection.get(user_id)
    if session_key:
        return session_key.decode('utf-8')
    else:
        return None
