from Pages.BasePage import BasePage
import random


class GoodsPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'inventory.html'

    def check_page(self):
        self.assert_valid_url_on_page()
        self.check_count_object(self.InventoryDescriptionSelector, 6)
        self.object_have_attribute(self.ImageTShirtSelector, 'src',
                                   '/static/media/bolt-shirt-1200x1500.c2599ac5.jpg')
        self.selector_have_text(self.T_SHIRTSELECTOR, 'Get your testing superhero on with the Sauce Labs bolt T-shirt.'
                                                      ' From American Apparel, 100% ringspun combed cotton,'
                                                      ' heather gray with red bolt.')
        self.selector_have_text(self.T_SHIRT_PRICE_SELECTOR, "$15.99")
        self.selector_have_text(self.T_SHIRT_NAME_SELECTOR, 'Sauce Labs Bolt T-Shirt')

        self.object_have_attribute(self.ImageBagSelector, 'src',
                                   '/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg')
        self.selector_have_text(self.BAG_TEXT_SELECTOR, 'carry.allTheThings() with the sleek, streamlined Sly Pack '
                                                        'that melds uncompromising style with unequaled'
                                                        ' laptop and tablet protection.')
        self.selector_have_text(self.BAG_PRICE_SELECTOR, "$29.99")
        self.selector_have_text(self.BAG_NAME_SELECTOR, 'Sauce Labs Backpack')

        self.object_have_attribute(self.ImageBikeSelector, 'src',
                                   '/static/media/bike-light-1200x1500.37c843b0.jpg')
        self.selector_have_text(self.BYCICLE_SELECTOR, "A red light isn't the desired state in testing but it "
                                                       "sure helps when riding your bike at night. Water-resistant with"
                                                       " 3 lighting modes, 1 AAA battery included.")
        self.selector_have_text(self.BYCICLE_PRICE_SELECTOR, "$9.99")
        self.selector_have_text(self.BYCICLE_NAME_SELECTOR, 'Sauce Labs Bike Light')

        self.object_have_attribute(self.ImageHoodieSelector, 'src',
                                   '/static/media/sauce-pullover-1200x1500.51d7ffaf.jpg')
        self.selector_have_text(self.HOODIE_SELECTOR, "It's not every day that you come across a midweight "
                                                      "quarter-zip fleece jacket capable of handling everything from a "
                                                      "relaxing day outdoors to a busy day at the office.")
        self.selector_have_text(self.HOODIE_PRICE_SELECTOR, "$49.99")
        self.selector_have_text(self.HOODIE_NAME_SELECTOR, 'Sauce Labs Fleece Jacket')

        self.object_have_attribute(self.ItemPolzunkiSelector, 'src',
                                   '/static/media/red-onesie-1200x1500.2ec615b2.jpg')
        self.selector_have_text(self.POLZUNKI_SELECTOR, "Rib snap infant onesie for the junior automation engineer "
                                                        "in development. Reinforced 3-snap bottom closure, two-needle "
                                                        "hemmed sleeved and bottom won't unravel.")
        self.selector_have_text(self.POLZUNKI_PRICE_SELECTOR, "$7.99")
        self.selector_have_text(self.POLZUNKI_NAME_SELECTOR, 'Sauce Labs Onesie')

        self.object_have_attribute(self.ItemRedSwitshotSelector, 'src',
                                   '/static/media/red-tatt-1200x1500.30dadef4.jpg')
        self.selector_have_text(self.RED_SWITSHOT_SELECTOR, "This classic Sauce Labs t-shirt is perfect to wear "
                                                            "when cozying up to your keyboard to automate a few tests."
                                                            " Super-soft and comfy ringspun combed cotton.")
        self.selector_have_text(self.RED_SWITSHOT_PRICE_SELECTOR, "$15.99")
        self.selector_have_text(self.RED_NAME_SELECTOR, 'Test.allTheThings() T-Shirt (Red)')

    def take_goods_in_cart(self):
        goods = (self.REDSWITSHOT_ADDSelector, self.BAG_ADDSelector, self.HOODIE_ADDSelector,
                 self.POLZUNKI_ADDSelector, self.T_SHIRT_ADDSelector, self.BYCICLE_ADDSelector)
        for i in goods:
            self.selector_ready_to_click(i)
            self.element_is_hidden(i)

    def remove_goods(self):
        remove = (self.BAG_RemoveSelector, self.BYCICLE_RemoveSelector, self.T_SHIRT_RemoveSelector,
                  self.HOODIE_RemoveSelector, self.REDSWITSHOT_RemoveSelector, self.POLZUNKI_RemoveSelector)
        for i in remove:
            self.selector_ready_to_click(i)
            self.element_is_hidden(i)

    def add_random_good_in_cart_and_check_cart(self):
        selectors = (self.REDSWITSHOT_ADDSelector, self.BAG_ADDSelector, self.HOODIE_ADDSelector,
                     self.POLZUNKI_ADDSelector, self.T_SHIRT_ADDSelector, self.BYCICLE_ADDSelector)
        self.selector_ready_to_click(random.choice(selectors))
        self.attribute_is_visible_and_count(self.CountOfGoodsInShoppingCart, '1')
        self.page.get_by_role('button', name='Remove').click()
        self.element_is_hidden(self.CountOfGoodsInShoppingCart)

    def add_red_switshot_good_in_cart(self):
        self.selector_ready_to_click(self.REDSWITSHOT_ADDSelector)

    def add_Tshirt_in_cart(self):
        self.selector_ready_to_click(self.T_SHIRT_ADDSelector)

    def remove_good_from_cart(self):
        self.selector_ready_to_click(self.REDSWITSHOT_RemoveSelector)
        self.attribute_is_visible_and_count(self.CountOfGoodsInShoppingCart, '1')

    def go_to_cart(self):
        self.selector_ready_to_click(self.ShoppingCartSelector)
        self.assert_text_next_page('Your Cart')
