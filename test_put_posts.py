import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestUpdatePost:

    def test_update_post_success(self):
        """Позитивный: обновление существующего поста."""
        data = {"title": "Updated Title", "body": "New body"}
        response = requests.put(f"{BASE_URL}/posts/1", json=data)
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Title"

    def test_update_post_wrong_method(self):
        """Негативный: использование GET вместо PUT."""
        response = requests.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200
        assert "title" in response.json()