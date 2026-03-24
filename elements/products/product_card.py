from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class ProductCardElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._card = page.locator('.product-image-wrapper')

    @classmethod
    def scoped(cls, page: Page, root: Locator) -> 'ProductCardElement':
        instance = cls.__new__(cls)
        instance.page = page
        instance._card = root.locator('.product-image-wrapper')
        return instance

    @property
    def image(self) -> Locator:
        return self._card.locator('.single-products img')

    @property
    def price(self) -> Locator:
        return self._card.locator('.productinfo.text-center h2')

    @property
    def name(self) -> Locator:
        return self._card.locator('.productinfo.text-center p')

    @property
    def add_to_cart_button(self) -> Locator:
        return self._card.locator('.productinfo.text-center a')

    @property
    def overlay_add_to_cart_button(self) -> Locator:
        return self._card.locator('.product-overlay a')

    @property
    def view_product_link(self) -> Locator:
        return self._card.locator('.choose a')
