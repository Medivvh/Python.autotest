from Pages.BasePage import BasePage


class CheckoutInfoPage(BasePage):
    FirstNameSelector = '#first-name'
    SecondNameSelector = '#last-name'
    PostalCodeSelector = '#postal-code'
    ContinueSelector = '#continue'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-one.html'

    def check_page(self):
        self.assert_valid_url_on_page()

    def place_order(self, name, secondname, postal):
        self.type_text_in_selector(self.FirstNameSelector, name)
        self.type_text_in_selector(self.SecondNameSelector, secondname)
        self.fill_text_in_selector(self.PostalCodeSelector, postal)
        self.selector_ready_to_click(self.ContinueSelector)
        self.assert_text_next_page('Checkout: Overview')
