import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_e2e_checkout_sampai_selesai(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)

    # 1. Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 2. Tambah produk ke keranjang & masuk ke halaman checkout
    inventory_page.add_backpack_to_cart()
    inventory_page.cart_link.click()
    page.locator("#checkout").click()

    # 3. Isi form data pengiriman
    checkout_page.fill_information("Muhammad", "Aqza", "40123")

    # 4. Selesaikan transaksi
    checkout_page.finish_checkout()

    # 5. Verifikasi pesan sukses transaksi
    assert checkout_page.get_completion_message() == "Thank you for your order!"