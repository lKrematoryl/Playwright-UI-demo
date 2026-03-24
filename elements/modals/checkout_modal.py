from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class CheckoutModalElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._modal = page.locator('#checkoutModal')

    @property
    def heading(self) -> Locator:
        return self._modal.get_by_role('heading', name='Checkout')

    @property
    def message(self) -> Locator:
        return self._modal.get_by_text('Register / Login account to proceed on checkout.')

    @property
    def register_login_link(self) -> Locator:
        return self._modal.get_by_role('link', name='Register / Login')

    @property
    def continue_on_cart_button(self) -> Locator:
        return self._modal.get_by_role('button', name='Continue On Cart')
