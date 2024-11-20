import pytest
from app import db
from app.modules.conftest import login, logout


def test_view_profile_with_login(test_client):

    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/profile/2")
    assert response.status_code == 200, "The profile page could not be accessed."


def test_view_profile_without_login(test_client):
    response = test_client.get("/profile/2")
    assert response.status_code == 200, "The profile page could not be accessed."

