from Pages.BasePage import BasePage


class CheckoutStep2(BasePage):
    FinishCheckoutSelector = '#finish'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-two.html'

    def finish_order(self):
        self.assert_valid_url_on_page()
        self.selector_ready_to_click(self.FinishCheckoutSelector)
        self.assert_text_next_page('Thank you for your order!')