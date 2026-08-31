import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestGetPosts:

    def test_get_posts_list(self):
        """Позитивный: получение списка постов."""
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_get_post_not_found(self):
        """Негативный: запрос несуществующего поста."""
        response = requests.get(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404