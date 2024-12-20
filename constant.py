BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}

"""GOODS SELECTORS"""
# ADD GOODS TO CART
REDSWITSHOT_ADDSelector = '#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)'
T_SHIRT_ADDSelector = '#add-to-cart-sauce-labs-bolt-t-shirt'
BYCICLE_ADDSelector = '#add-to-cart-sauce-labs-bike-light'
BAG_ADDSelector = '#add-to-cart-sauce-labs-backpack'
HOODIE_ADDSelector = '#add-to-cart-sauce-labs-fleece-jacket'
POLZUNKI_ADDSelector = '#add-to-cart-sauce-labs-onesie'
# REMOVE GOODS FROM CART
REDSWITSHOT_RemoveSelector = '#remove-test\.allthethings\(\)-t-shirt-\(red\)'
BAG_RemoveSelector = '#remove-sauce-labs-backpack'
T_SHIRT_RemoveSelector = '#remove-sauce-labs-bolt-t-shirt'
HOODIE_RemoveSelector = '#remove-sauce-labs-fleece-jacket'
POLZUNKI_RemoveSelector = '#remove-sauce-labs-onesie'
BYCICLE_RemoveSelector = '#remove-sauce-labs-bike-light'
# CART SELECTOR
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

# NAME_ITEM_SELECTOR
BAG_NAME_SELECTOR = '#item_4_title_link > div'
BYCICLE_NAME_SELECTOR = '#item_0_title_link > div'
T_SHIRT_NAME_SELECTOR = '#item_1_title_link > div'
HOODIE_NAME_SELECTOR = '#item_5_title_link > div'
POLZUNKI_NAME_SELECTOR = '#item_2_title_link > div'
RED_NAME_SELECTOR = '#item_3_title_link > div'

# SELECTOR OPISANIE
BAG_TEXT_SELECTOR = (
    '#inventory_container > div > div:nth-child(1) > '
    'div.inventory_item_description > div.inventory_item_label > div')
T_SHIRTSELECTOR = ('#inventory_container > div > div:nth-child(3) > '
                   'div.inventory_item_description > div.inventory_item_label > div')
BYCICLE_SELECTOR = ('#inventory_container > div > div:nth-child(2) > '
                    'div.inventory_item_description > div.inventory_item_label > div')
HOODIE_SELECTOR = ('#inventory_container > div > div:nth-child(4) > '
                   'div.inventory_item_description > div.inventory_item_label > div')
POLZUNKI_SELECTOR = ('#inventory_container > div > div:nth-child(5) > '
                     'div.inventory_item_description > div.inventory_item_label > div')
RED_SWITSHOT_SELECTOR = ('#inventory_container > div > div:nth-child(6) > '
                         'div.inventory_item_description > div.inventory_item_label > div')

# SELECTOR_PRICES
BAG_PRICE_SELECTOR = ('#inventory_container > div > div:nth-child(1) > '
                      'div.inventory_item_description > div.pricebar > div')
BYCICLE_PRICE_SELECTOR = ('#inventory_container > div > div:nth-child(2) > '
                          'div.inventory_item_description > div.pricebar > div')
T_SHIRT_PRICE_SELECTOR = ('#inventory_container > div > div:nth-child(3) > '
                          'div.inventory_item_description > div.pricebar > div')
HOODIE_PRICE_SELECTOR = ('#inventory_container > div > div:nth-child(4) > '
                         'div.inventory_item_description > div.pricebar > div')
POLZUNKI_PRICE_SELECTOR = ('#inventory_container > div > div:nth-child(5) > '
                           'div.inventory_item_description > div.pricebar > div')
RED_SWITSHOT_PRICE_SELECTOR = ('#inventory_container > div > div:nth-child(6) > '
                               'div.inventory_item_description > div.pricebar > div')
