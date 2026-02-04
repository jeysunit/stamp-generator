from fastapi.testclient import TestClient

from app.main import app


def test_index_returns_ok():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "スタンプ画像生成" in response.text
