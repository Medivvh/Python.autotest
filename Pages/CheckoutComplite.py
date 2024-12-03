from Pages import BasePage


class CheckoutComplite(BasePage):
    CheckoutPageSelector = '#checkout_complete_container > img'
    BackHomeButtonSelector = '#back-to-products'
    BurgerMenuButtonSelector = '#react-burger-menu-btn'
    AllItemsInBurgerSelector = '#inventory_sidebar_link'
    AboutInBurgerSelector = '#about_sidebar_link'
    LogoutInBurgerSelector = '#logout_sidebar_link'
    ResetAppInBurgerSelector = '#reset_sidebar_link'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-complete.html'

    def check_main_elements(self):
        self.bject_is_visible_and_enabled(self.CheckoutPageSelector)
        self.bject_is_visible_and_enabled(self.BackHomeButtonSelector)

    def check_burger_and_logout(self):
        self.selector_ready_to_click(self.BurgerMenuButtonSelector)
        self.bject_is_visible_and_enabled(self.AllItemsInBurgerSelector)
        self.bject_is_visible_and_enabled(self.AboutInBurgerSelector)
        self.bject_is_visible_and_enabled(self.ResetAppInBurgerSelector)
        self.selector_ready_to_click(self.LogoutInBurgerSelector)
        self.assert_text_next_page(self, 'Login')
