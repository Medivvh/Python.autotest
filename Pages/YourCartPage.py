from Pages.BasePage import BasePage


class YourCartPage(BasePage):
    GoodInCartSelector = '#cart_contents_container > div > div.cart_list > div.cart_item'
    CheckoutSelector = '#checkout'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html'

    def cart_have_good(self):
        self.assert_valid_url_on_page()
        self.assert_text_next_page('T-Shirt')

    def checkout(self):
        self.selector_ready_to_click(self.CheckoutSelector)
        self.assert_text_next_page('Checkout: Your Information')
