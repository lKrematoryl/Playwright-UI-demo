from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class OrderPlacedElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('section#form')

    @property
    def heading(self) -> Locator:
        return self._section.get_by_role('heading', name='Order Placed!')

    @property
    def congratulations_text(self) -> Locator:
        return self._section.get_by_text('Congratulations! Your order has been confirmed!')

    @property
    def download_invoice_button(self) -> Locator:
        return self._section.get_by_role('link', name='Download Invoice')

    @property
    def continue_button(self) -> Locator:
        return self._section.get_by_role('link', name='Continue')
