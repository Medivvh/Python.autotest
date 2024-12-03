from Pages.BasePage import BasePage


class GoodsPage(BasePage):
    FirstGoodADDSelector = '#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)'
    SecondGoodADDSelector = '#add-to-cart-sauce-labs-bolt-t-shirt'
    FirstGoodRemoveSelector = '#remove-test\.allthethings\(\)-t-shirt-\(red\)'
    ShoppingCartSelector = '#shopping_cart_container > a > span'
    CountOfGoodsInShoppingCart = '.shopping_cart_badge'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'


    def add_first_good_in_cart(self):
        self.selector_ready_to_click(self.FirstGoodADDSelector)


    def add_second_good_in_cart(self):
        self.selector_ready_to_click(self.SecondGoodADDSelector)


    def remove_good_from_cart(self):
        self.selector_ready_to_click(self.FirstGoodRemoveSelector)


    def go_to_cart(self):
        self.selector_ready_to_click(self.ShoppingCartSelector)
        self.assert_text_next_page('Your Cart')
