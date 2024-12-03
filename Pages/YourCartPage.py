from Pages import BasePage


class YourCartPage(BasePage):
    GoodInCartSelector = '#cart_contents_container > div > div.cart_list > div.cart_item'
    CheckoutSelector = '#checkout'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html'

    def cart_have_good(self):
        self.assert_text_next_page(self.GoodInCartSelector, 'Test.allTheThings() T-Shirt (Red)')

    def checkout(self):
        self.selector_ready_to_click(self.CheckoutSelector)
        self.assert_text_next_page(self, 'Checkout: Your Information')
