from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement
from elements.product_card import ProductCardElement


class FeaturesItemsElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('.features_items')
        self.product_card = ProductCardElement.scoped(page, self._section)

    @property
    def heading(self) -> Locator:
        return self._section.get_by_role('heading', name='Features Items')
