import requests
import logging


def get_posts(base_url):
    url = f"{base_url}/posts"
    logging.info(f"GET {url}")
    response = requests.get(url)
    logging.info(f"Response: {response.status_code}")
    return response


def get_post_by_id(base_url, post_id):
    url = f"{base_url}/posts/{post_id}"
    logging.info(f"GET {url}")
    response = requests.get(url)
    logging.info(f"Response: {response.status_code}")
    return response
