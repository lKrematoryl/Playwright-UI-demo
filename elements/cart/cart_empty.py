from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class CartEmptyElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('#empty_cart')

    @property
    def message(self) -> Locator:
        return self._section.get_by_text('Cart is empty!')

    @property
    def buy_products_link(self) -> Locator:
        return self._section.get_by_role('link', name='here')
