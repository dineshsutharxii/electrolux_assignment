import requests


def get_posts(base_url):
    return requests.get(f"{base_url}/posts")


def get_post_by_id(base_url, post_id):
    return requests.get(f"{base_url}/posts/{post_id}")
