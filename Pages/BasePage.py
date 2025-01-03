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
        expect(self.page.locator(selector)).to_be_visible()
        expect(self.page.locator(selector)).to_be_enabled()
        self.page.click(selector)

    def type_text_in_selector(self, selector, text):
        """
        Селектор видимый, печатаем
        """
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.type(selector, text)

    def fill_text_in_selector(self, selector, value):
        """
        Селектор видимый, заполняем
        """
        self.page.wait_for_selector(selector)
        self.page.is_visible(selector)
        self.page.fill(selector, value)

    def attribute_is_visible_and_count(self, selector, text):
        self.page.wait_for_selector(selector)
        expect(self.page.locator(selector)).to_have_text(text)

    def object_is_visible_and_enabled(self, selector):
        expect(self.page.locator(selector)).to_be_visible()
        expect(self.page.locator(selector)).to_be_enabled()

    def selector_have_text(self, selector, text):
        self.page.is_visible(selector)
        expect(self.page.locator(selector)).to_contain_text(text)

    def element_is_hidden(self, selector):
        expect(self.page.locator(selector)).to_be_hidden()

    def assert_text_next_page(self, text):
        """
        Проверяем наличия текста в теле страницы
        """
        expect(self.page.locator("body")).to_contain_text(text)

    def find_element_by_role_and_text(self, role, text):
        self.page.get_by_role(role, text)

    def assert_valid_url_on_page(self):
        expect(self.page).to_have_url(self._full_url())

    def check_count_object(self, selector, count):
        expect(self.page.locator(selector)).to_have_count(count)

    def object_have_attribute(self, selector, name, attribute):
        expect(self.page.locator(selector)).to_have_attribute(name, attribute)
