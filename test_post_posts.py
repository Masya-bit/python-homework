import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestCreatePost:

    def test_create_post_success(self):
        """Позитивный: создание поста с корректными данными."""
        data = {"title": "Test", "body": "Hello", "userId": 1}
        response = requests.post(f"{BASE_URL}/posts", json=data)
        assert response.status_code == 201
        assert response.json()["title"] == "Test"
        assert "id" in response.json()

    def test_create_post_invalid_data(self):
        """Негативный: создание поста с некорректным типом данных."""
        data = {"title": 12345, "body": "Hello", "userId": "не число"}
        response = requests.post(f"{BASE_URL}/posts", json=data)
        assert response.status_code == 201
        body = response.json()
        assert body["title"] == 12345