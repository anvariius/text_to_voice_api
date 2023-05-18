from fastapi.testclient import TestClient
from main import app
import json

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "FastAPI is active"}

def test_result():
    response = client.get("/text_to_voice/hello")
    assert response.status_code == 200
    assert response.json()['result'] == "text is voiced"

def test_download():
    response = client.get("/download_voice/cffkgwrb.mp3")
    assert response.status_code == 200