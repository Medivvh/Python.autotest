from Pages.BasePage import BasePage


class LoginPage(BasePage):
    UsernameSelector = '#user-name'
    PasswordSelector = '#password'
    LoginButtonSelector = '.submit-button'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def login(self, username, password):
        self.go_to_full_url()
        self.type_text_in_selector(self.UsernameSelector, username)
        self.fill_text_in_selector(self.PasswordSelector, password)
        self.selector_ready_to_click(self.LoginButtonSelector)
        self.assert_text_next_page('Products')
