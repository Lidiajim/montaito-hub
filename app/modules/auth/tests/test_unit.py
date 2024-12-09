import pytest
from flask import url_for

from app.modules.auth.services import AuthenticationService
from app.modules.auth.repositories import UserRepository
from app.modules.profile.repositories import UserProfileRepository


@pytest.fixture(scope="module")
def test_client(test_client):
    """
    Extends the test_client fixture to add additional specific data for module testing.
    """
    with test_client.application.app_context():
        # Add HERE new elements to the database that you want to exist in the test context.
        # DO NOT FORGET to use db.session.add(<element>) and db.session.commit() to save the data.
        pass

    yield test_client


def test_login_success(test_client):
    response = test_client.post(
        "/login", data=dict(email="test@example.com", password="test1234"), follow_redirects=True
    )

    assert response.request.path != url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_login_unsuccessful_bad_email(test_client):
    response = test_client.post(
        "/login", data=dict(email="bademail@example.com", password="test1234"), follow_redirects=True
    )

    assert response.request.path == url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_login_unsuccessful_bad_password(test_client):
    response = test_client.post(
        "/login", data=dict(email="test@example.com", password="basspassword"), follow_redirects=True
    )

    assert response.request.path == url_for("auth.login"), "Login was unsuccessful"

    test_client.get("/logout", follow_redirects=True)


def test_signup_user_no_name(test_client):
    response = test_client.post(
        "/signup", data=dict(surname="Foo", email="test@example.com", password="test1234"), follow_redirects=True
    )
    assert response.request.path == url_for("auth.show_signup_form"), "Signup was unsuccessful"
    assert b"This field is required" in response.data, response.data


def test_signup_user_unsuccessful(test_client):
    email = "test@example.com"
    response = test_client.post(
        "/signup", data=dict(name="Test", surname="Foo", email=email, password="test1234"), follow_redirects=True
    )
    assert response.request.path == url_for("auth.show_signup_form"), "Signup was unsuccessful"
    assert f"Email {email} in use".encode("utf-8") in response.data


def test_signup_user_successful(test_client):
    response = test_client.post(
        "/signup",
        data=dict(name="Foo", surname="Example", email="foo@example.com", password="foo1234"),
        follow_redirects=True,
    )
    assert response.request.path == url_for("public.index"), "Signup was unsuccessful"


def test_service_create_with_profie_success(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "service_test@example.com",
        "password": "test1234"
    }

    AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 1
    assert UserProfileRepository().count() == 1


def test_service_create_with_profile_fail_no_email(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "",
        "password": "1234"
    }

    with pytest.raises(ValueError, match="Email is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0


def test_service_create_with_profile_fail_no_password(clean_database):
    data = {
        "name": "Test",
        "surname": "Foo",
        "email": "test@example.com",
        "password": ""
    }

    with pytest.raises(ValueError, match="Password is required."):
        AuthenticationService().create_with_profile(**data)

    assert UserRepository().count() == 0
    assert UserProfileRepository().count() == 0

def test_reset_password_mismatched_passwords(test_client, clean_database):
    data = {
        "name": "Test",
        "surname": "User",
        "email": "mismatched_passwords@example.com",
        "password": "password123"
    }
    user = AuthenticationService().create_with_profile(**data)
    token = AuthenticationService().generate_password_reset_token(user.email)

    reset_url = f"/reset_password/{token}"
    response = test_client.post(
        reset_url,
        data={"password": "newpassword123", "password_confirm": "differentpassword123"},
        follow_redirects=True
    )

    print(response.data.decode())

    assert b"Passwords do not match" in response.data or b"confirm_password" in response.data, \
        "The response does not indicate mismatched passwords"


def test_remember_password_invalid_email(test_client, clean_database):
    response = test_client.post(
        "/remember_my_password",
        data={"email": "nonexistent_user@example.com"},
        follow_redirects=True
    )

    response_text = response.data.decode()
    print("Response HTML:", response_text)

    assert response.status_code == 200, "Unexpected status code"


def test_remember_password_email_sent(test_client, clean_database):
    data = {
        "name": "Test",
        "surname": "User",
        "email": "user_test@example.com",
        "password": "password123"
    }
    AuthenticationService().create_with_profile(**data)

    response = test_client.post("/remember_my_password", 
                                data={"email": "user_test@example.com"}, 
                                follow_redirects=True)

    assert response.status_code == 200, "Unexpected status code"
