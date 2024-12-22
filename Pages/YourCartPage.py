from Pages.BasePage import BasePage


class YourCartPage(BasePage):
    GoodInCartSelector = '#cart_contents_container > div > div.cart_list > div.cart_item'
    CheckoutSelector = '#checkout'
    InventorySelector = '#cart_contents_container > div > div.cart_list'
    ContinueShoppingSelector = '#continue-shopping'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html'

    def cart_have_good(self):
        self.assert_valid_url_on_page()
        self.assert_text_next_page('T-Shirt')

    def checkout(self):
        self.selector_ready_to_click(self.CheckoutSelector)
        self.assert_text_next_page('Checkout: Your Information')

    def cart_have_object(self):
        self.assert_valid_url_on_page()
        self.check_count_object(self.InventorySelector, 1)
        self.page.get_by_role('button', name='Remove').is_visible()
        self.page.get_by_role('button', name='Remove').is_enabled()
        self.object_is_visible_and_enabled(self.ContinueShoppingSelector)

    def empty_cart(self):
        self.assert_valid_url_on_page()
        self.check_count_object(self.InventorySelector, 0)
        self.page.get_by_role('button', name='Remove').is_visible()
        self.page.get_by_role('button', name='Remove').is_enabled()
        self.object_is_visible_and_enabled(self.ContinueShoppingSelector)
