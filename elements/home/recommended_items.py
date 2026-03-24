from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class RecommendedItemsElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('.recommended_items')

    @property
    def heading(self) -> Locator:
        return self._section.get_by_role('heading', name='recommended items')

    @property
    def active_slide(self) -> Locator:
        return self._section.locator('.item.active')

    @property
    def item_image(self) -> Locator:
        return self.active_slide.locator('.productinfo img')

    @property
    def item_price(self) -> Locator:
        return self.active_slide.locator('.productinfo h2')

    @property
    def item_name(self) -> Locator:
        return self.active_slide.locator('.productinfo p')

    @property
    def add_to_cart_button(self) -> Locator:
        return self.active_slide.locator('a.add-to-cart')
