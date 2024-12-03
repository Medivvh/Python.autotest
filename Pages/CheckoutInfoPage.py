from Pages import BasePage


class CheckoutInfoPage(BasePage):
    FirstNameSelector = '#first-name'
    SecondNameSelector = '#last-name'
    PostalCodeSelector = '#postal-code'
    ContinueSelector = '#continue'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'cart.html'

    def place_order(self, name, secondname, postal):
        self.type_text_in_selector(self.FirstNameSelector, name, 500)
        self.type_text_in_selector(self.SecondNameSelector, secondname, 500)
        self.fill_text_in_selector(self.PostalCodeSelector, postal, 100)
        self.selector_ready_to_click(self.ContinueSelector)
        self.assert_text_next_page(self, 'Checkout: Overview')
