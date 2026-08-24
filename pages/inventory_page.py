class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.add_to_cart_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()