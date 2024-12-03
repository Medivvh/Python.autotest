from playwright.sync_api import expect


class BasePage:
    __BaseURL = 'https://www.saucedemo.com'

    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    def _full_url(self):
        return f'{self.__BaseURL}/{self._endpoint}'

    def go_to_full_url(self):
        """
        Переход по url с ожиданием загрузки и проверкой видимости
        """
        full_url = self._full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def selector_ready_to_click(self, selector):
        """
        Кнопка видима, активна. Нажимаем
        """
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.is_enabled(selector)
        self.page.click(selector)

    def type_text_in_selector(self, selector, text):
        """
        Селектор видимый, печатаем, проверяем что заполнен
        """
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.type(selector, text)


    def fill_text_in_selector(self, selector, value):
        """
        Селектор видимый, копируем, проверяем что заполнен
        """
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.fill(selector, value)


    def object_is_visible_and_enabled(self, selector):
        self.page.is_visible(selector)
        self.page.is_enabled(selector)


    def assert_text_next_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)
