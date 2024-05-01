import requests
import redis
from functools import wraps

def cache_decorator(func):
    @wraps(func)
    def wrapper(url):
        # Initialize Redis client
        redis_client = redis.Redis()

        # Check if the page content is cached
        cached_content = redis_client.get(url)
        if cached_content:
            return cached_content.decode('utf-8')

        # Call the original function if the content is not cached
        content = func(url)

        # Cache the page content with an expiration time of 10 seconds
        redis_client.setex(url, 10, content)

        return content
    return wrapper

@cache_decorator
def get_page_with_cache(url: str) -> str:
    # Retrieve page content using requests
    response = requests.get(url)
    return response.text

# Usage example:
url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.com"
content = get_page_with_cache(url)
print(content)

