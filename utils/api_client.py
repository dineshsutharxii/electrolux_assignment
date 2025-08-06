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


def add_new_post(base_url, payload):
    url = f"{base_url}/posts"
    logging.info(f'Post {url}')
    response = requests.post(url=url, json=payload)
    logging.info(f"Response: {response.status_code}")
    logging.info(f"Response: {response.json()}")
    return response


def update_post(base_url, payload, id):
    url = f"{base_url}/posts/{id}"
    logging.info(f'Put {url}')
    response = requests.put(url=url, json=payload)
    logging.info(f"Response: {response.status_code}")
    logging.info(f"Response: {response.json()}")
    return response


def delete_post(base_url, id):
    url = f"{base_url}/posts/{id}"
    logging.info(f'Delete {url}')
    response = requests.put(url=url)
    logging.info(f"Response: {response.status_code}")
    logging.info(f"Response: {response.json()}")
    return response
