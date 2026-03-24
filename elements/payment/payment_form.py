from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class PaymentFormElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('#payment-form')

    @property
    def heading(self) -> Locator:
        return self.page.locator('div.step-one').get_by_role('heading', name='Payment')

    @property
    def name_on_card_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Name on Card')

    @property
    def card_number_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Card Number')

    @property
    def cvc_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='CVC')

    @property
    def expiry_month_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Expiration')

    @property
    def expiry_year_input(self) -> Locator:
        return self._section.locator('input[name="expiry_year"]')

    @property
    def pay_and_confirm_button(self) -> Locator:
        return self._section.get_by_role('button', name='Pay and Confirm Order')

    @property
    def success_message(self) -> Locator:
        return self._section.locator('#success_message')
