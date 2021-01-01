from fastapi.testclient import TestClient

from campaign.main import app

client = TestClient(app)
