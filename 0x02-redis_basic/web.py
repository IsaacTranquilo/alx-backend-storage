import requests
import redis

def get_page(url: str) -> str:
    # Initialize Redis client
    redis_client = redis.Redis()

    # Track the number of times the URL was accessed
    count_key = f"count:{url}"
    redis_client.incr(count_key)

    # Check if the page content is cached
    cached_content = redis_client.get(url)
    if cached_content:
        return cached_content.decode('utf-8')

    # Retrieve page content using requests
    response = requests.get(url)
    content = response.text

    # Cache the page content with an expiration time of 10 seconds
    redis_client.setex(url, 10, content)

    return content

