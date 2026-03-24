from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class OrderCommentElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('#ordermsg')

    @property
    def comment_input(self) -> Locator:
        return self._section.get_by_role('textbox')

    @property
    def place_order_button(self) -> Locator:
        return self.page.get_by_role('link', name='Place Order')
