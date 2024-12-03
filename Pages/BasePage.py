from playwright.sync_api import expect


class BasePage:
    BaseURL = 'https://www.saucedemo.com'

    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    def _full_url(self):
        return f'{self.BaseURL}/{self._endpoint}'

    def go_to_full_url(self):
        """
        Переход по url с ожиданием загрузки и проверкой видимости
        """
        full_url = self._full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(self.BaseURL)

    def selector_ready_to_click(self, selector):
        """
        Кнопка видима, активна. Нажимаем
        """
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.is_enable(selector)
        self.page.click(selector)

    def type_text_in_selector(self, selector, text, delay):
        """
        Селектор видимый, печатаем, проверяем что заполнен
        """
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.type(selector, text, delay)
        expect(self.page).not_to_be_empty(selector)

    def fill_text_in_selector(self, selector, value, delay):
        """
        Селектор видимый, копируем, проверяем что заполнен
        """
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.fill(selector, value, delay)
        expect(self.page).not_to_be_empty(selector)

    def load_to_body_have_text(self, selector, text):
        self.page.wait_for_selector(selector.to_have_text(text))

    def object_is_visible_and_enabled(self, selector):
        self.page.is_visible(selector)
        self.page.is_enable(selector)


    def url_is_valid(self):
        expect(self.page).to_have_url(self._full_url)

    def assert_that_selector_is_hidden(self, selector):
        expect(self.page).is_hidden(selector)

    def assert_text_next_page(self, text):
        expect(self.page.locator("body")).to_contain_text(text)
