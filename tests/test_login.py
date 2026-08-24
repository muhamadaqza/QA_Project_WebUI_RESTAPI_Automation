from pages.login_page import LoginPage

def test_login_sukses(page):
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")

    # Verifikasi berhasil masuk ke halaman inventory
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_login_gagal_password_salah(page):
    login_p = LoginPage(page)
    login_p.navigate()
    login_p.login("standard_user", "wrong_password")

    # Verifikasi pesan error muncul
    error_text = login_p.get_error_text()
    assert "Username and password do not match" in error_text