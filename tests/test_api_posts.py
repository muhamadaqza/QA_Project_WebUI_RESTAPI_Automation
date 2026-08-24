import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_api_post_by_id():
    with sync_playwright() as p:
        # 1. Inisialisasi API Request Context
        api_request = p.request.new_context(base_url=BASE_URL)

        # 2. Kirim GET Request ke endpoint /posts/1
        response = api_request.get("/posts/1")

        # 3. Assert HTTP Status Code 200 (OK)
        assert response.status == 200

        # 4. Assert struktur payload JSON
        body = response.json()
        assert body["id"] == 1
        assert "title" in body
        assert "body" in body

        api_request.dispose()

def test_create_new_api_post():
    with sync_playwright() as p:
        api_request = p.request.new_context(base_url=BASE_URL)

        # Payload data yang akan dikirim
        payload = {
            "title": "QA Automation Playwright",
            "body": "Testing REST API endpoints with Python & Pytest",
            "userId": 1
        }

        # 1. Kirim POST Request ke endpoint /posts
        response = api_request.post("/posts", data=payload)

        # 2. Assert HTTP Status Code 201 (Created)
        assert response.status == 201

        # 3. Assert respon JSON sesuai dengan data yang dikirim
        body = response.json()
        assert body["title"] == "QA Automation Playwright"
        assert body["userId"] == 1

        api_request.dispose()