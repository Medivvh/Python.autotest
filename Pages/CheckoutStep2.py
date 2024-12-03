from Pages import BasePage


class CheckoutStep2(BasePage):
    FinishCheckoutSelector = '#finish'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-two.html'

    def finish_order(self):
        self.url_is_valid()
        self.selector_ready_to_click(self.FinishCheckoutSelector)
        self.assert_text_next_page(self, 'Thank you for your order!')