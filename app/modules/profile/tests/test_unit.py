import pytest

from app import db
from app.modules.conftest import login, logout
from app.modules.auth.models import User
from app.modules.profile.models import UserProfile
from app.modules.auth.services import AuthenticationService


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        # Create a test user
        user_test = User(email='user@example.com', password='test1234')
        user_test.set_password("test1234")  # Set hashed password
        db.session.add(user_test)
        db.session.commit()

        # Create a profile for the user
        profile = UserProfile(user_id=user_test.id, name="Name", surname="Surname")
        db.session.add(profile)
        db.session.commit()

    yield test_client


def test_edit_profile_page_get(test_client):
    """
    Tests access to the profile editing page via a GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/profile/edit")
    assert response.status_code == 200, "The profile editing page could not be accessed."
    assert b"Edit profile" in response.data, "The expected content is not present on the page"

    logout(test_client)

@pytest.fixture
def auth_service(test_app):
    with test_app.app_context():
        return AuthenticationService()

def test_generate_password_reset_token(auth_service):
    token = auth_service.generate_password_reset_token("user@example.com")
    assert token, "Token generation failed."
    print(f"Generated token: {token}")


def test_generate_password_reset_link(test_client, auth_service):
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    with test_client.application.app_context():
        from flask_login import current_user
        print(f"Logged in user email: {current_user.email}")

    response = test_client.post("/profile/reset_password_link", follow_redirects=False)
    assert response.status_code == 302, "Expected a redirection but didn't get it."

    location = response.headers.get("Location")
    print(f"Redirection location: {location}") 

    assert location, "Redirection URL is None."
    assert "reset_password" in location, "Reset password link not included in the redirection URL."

    token = location.rsplit('/', 1)[-1] 
    print(f"Extracted token: {token}") 
    assert token, "The reset password link does not contain a token."

    logout(test_client)


def test_generate_token(auth_service):
    token = auth_service.generate_password_reset_token("user@example.com")
    assert token is not None, "Token generation failed."


def test_reset_password_flow(test_client, auth_service):
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    with test_client.application.app_context():
        from app.modules.auth.models import User
        user = User.query.filter_by(email="user@example.com").first()
        assert user, "Test user not found in the database."

        token = auth_service.generate_password_reset_token(user.email)
        assert token, "Failed to generate a reset password token."

    reset_password_url = f"/reset_password/{token}"
    response = test_client.get(reset_password_url)
    assert response.status_code == 200, "Failed to access the reset password page."

    new_password = "newpassword123"
    response = test_client.post(
        reset_password_url,
        data={
            "password": new_password,
            "password_confirm": new_password
        },
        follow_redirects=True
    )
    assert response.status_code == 200, "Failed to reset the password."

    logout(test_client)  
    login_response = login(test_client, "user@example.com", new_password)
    assert login_response.status_code == 200, "Login with the new password was unsuccessful."


def test_generate_password_reset_link_without_authentication(test_client):
    test_client.get("/logout", follow_redirects=True)

    response = test_client.post("/profile/reset_password_link", follow_redirects=False)

    assert response.status_code == 302, "Expected a redirection to the login page."
    assert "/login" in response.headers["Location"], "Redirection to login page not found."