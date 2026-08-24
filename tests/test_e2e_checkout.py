import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_e2e_tambah_produk_ke_keranjang(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 1. Buka halaman login & jalankan autentikasi
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Tambahkan produk ke keranjang belanja
    inventory_page.add_backpack_to_cart()

    # 3. Verifikasi jumlah item pada ikon keranjang
    assert inventory_page.get_cart_count() == "1"