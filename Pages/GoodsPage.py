from Pages.BasePage import BasePage


class GoodsPage(BasePage):
    FirstGoodADDSelector = '#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)'
    SecondGoodADDSelector = '#add-to-cart-sauce-labs-bolt-t-shirt'
    FirstGoodRemoveSelector = '#remove-test\.allthethings\(\)-t-shirt-\(red\)'
    ShoppingCartSelector = '#shopping_cart_container > a > span'
    CountOfGoodsInShoppingCart = '.shopping_cart_badge'
    InventoryDescriptionSelector = '.inventory_item_description'
    # Images
    ImageTShirtSelector = '#item_1_img_link > img'
    ImageBagSelector = '#item_4_img_link > img'
    ImageBikeSelector = '#item_0_img_link > img'
    ImageHoodieSelector = '#item_5_img_link > img'
    ItemPolzunkiSelector = '#item_2_img_link > img'
    ItemRedSwitshotSelector = '#item_3_img_link > img'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    def check_page(self):
        self.assert_valid_url_on_page()
        self.check_count_object(self.InventoryDescriptionSelector, 6)
        self.object_have_attribute(self.ImageTShirtSelector, 'src',
                                   '/static/media/bolt-shirt-1200x1500.c2599ac5.jpg')
        self.object_have_attribute(self.ImageBagSelector, 'src',
                                   '/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg')
        self.object_have_attribute(self.ImageBikeSelector, 'src',
                                   '/static/media/bike-light-1200x1500.37c843b0.jpg')
        self.object_have_attribute(self.ImageHoodieSelector, 'src',
                                   '/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg')
        self.object_have_attribute(self.ItemPolzunkiSelector, 'src',
                                   '/static/media/red-onesie-1200x1500.2ec615b2.jpg')
        self.object_have_attribute(self.ItemRedSwitshotSelector, 'src',
                                   '/static/media/red-tatt-1200x1500.30dadef4.jpg')

    def add_first_good_in_cart(self):
        self.selector_ready_to_click(self.FirstGoodADDSelector)
        self.element_is_hidden(self.FirstGoodADDSelector)
        self.object_is_visible_and_enabled(self.FirstGoodRemoveSelector)
        self.attribute_is_visible_and_count(self.CountOfGoodsInShoppingCart, '1')

    def add_second_good_in_cart(self):
        self.selector_ready_to_click(self.SecondGoodADDSelector)
        self.element_is_hidden(self.SecondGoodADDSelector)
        self.attribute_is_visible_and_count(self.CountOfGoodsInShoppingCart, '2')

    def remove_good_from_cart(self):
        self.selector_ready_to_click(self.FirstGoodRemoveSelector)
        self.attribute_is_visible_and_count(self.CountOfGoodsInShoppingCart, '1')

    def go_to_cart(self):
        self.selector_ready_to_click(self.ShoppingCartSelector)
        self.assert_text_next_page('Your Cart')
