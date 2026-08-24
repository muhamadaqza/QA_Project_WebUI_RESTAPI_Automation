import pytest
from pages.login_page import LoginPage

# Data-driven test untuk menguji berbagai skenario login sekaligus
@pytest.mark.parametrize("username, password, expected_url_part", [
    ("standard_user", "secret_sauce", "/inventory.html"),
    ("problem_user", "secret_sauce", "/inventory.html"),
    ("performance_glitch_user", "secret_sauce", "/inventory.html")
])
def test_login_multiple_accounts(page, username, password, expected_url_part):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)
    assert expected_url_part in page.url

def test_login_gagal_password_salah(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "wrong_password")

    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"