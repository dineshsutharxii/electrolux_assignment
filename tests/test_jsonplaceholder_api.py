import pytest
#from electrolux_assignment.utils.api_client import get_posts, get_post_by_id
from utils.api_client import get_posts, get_post_by_id, add_new_post, update_post, delete_post


def test_get_all_posts(base_url):
    response = get_posts(base_url)
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0
    for post in posts:
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post


@pytest.mark.parametrize("post_id", [1, 5, 10, 50, 100])
def test_get_post_by_valid_id(base_url, post_id, expected_posts):
    response = get_post_by_id(base_url, post_id)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert post["title"] == expected_posts[post_id]["title"]
    assert post["body"] == expected_posts[post_id]["body"]
    assert isinstance(post["title"], str)


@pytest.mark.parametrize("invalid_id", [0, 101, 9999, -5])
def test_get_post_by_invalid_id(base_url, invalid_id):
    response = get_post_by_id(base_url, invalid_id)
    assert response.status_code == 404 or response.json() == {}


@pytest.mark.parametrize('payload', [
    {
        "userId": 1,
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
    },
    {
        "userId": 1,
        "title": "eum et est occaecati",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
    },
    {
        "userId": 1,
        "title": "nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
    }
])
def test_add_new_post(base_url, payload):
    response = add_new_post(base_url, payload)
    assert response.status_code == 201
    json_res = response.json()
    assert json_res['title'] == payload['title']
    assert json_res['body'] == payload['body']


@pytest.mark.parametrize("post_id, payload", [(1, {"id": 1, "title": "Post One", "body": "Body One", "userId": 1}),
                                              (5, {"id": 5, "title": "Post Five", "body": "Body Five", "userId": 1}),
                                              (10, {"id": 10, "title": "Post ten", "body": "Body ten", "userId": 1})])
def test_update_post(base_url, post_id, payload):
    response = update_post(base_url, payload, post_id)
    assert response.status_code == 200
    json_res = response.json()
    assert json_res['title'] == payload['title']
    assert json_res['body'] == payload['body']


@pytest.mark.parametrize("post_id", [1, 5, 10, 50, 100])
def test_delete_post(base_url, post_id):
    response = delete_post(base_url, post_id)
    assert response.status_code == 200
