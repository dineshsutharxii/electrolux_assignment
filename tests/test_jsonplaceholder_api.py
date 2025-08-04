import pytest
from utils.api_client import get_posts, get_post_by_id

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
def test_get_post_by_valid_id(base_url, post_id):
    response = get_post_by_id(base_url, post_id)
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id
    assert isinstance(post["title"], str)

@pytest.mark.parametrize("invalid_id", [0, 101, 9999, -5])
def test_get_post_by_invalid_id(base_url, invalid_id):
    response = get_post_by_id(base_url, invalid_id)
    assert response.status_code == 404 or response.json() == {}
