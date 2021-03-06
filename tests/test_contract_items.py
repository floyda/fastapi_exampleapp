
from uuid import uuid4

import pytest
from app import api
from fastapi.testclient import TestClient

client = TestClient(api)


@pytest.fixture()
def resource_mock_items(mocker):
    return {}


def test_get_all_todos(resource_mock_items):
    response = client.get("/todos")
    # response.
    assert response.status_code == 200
