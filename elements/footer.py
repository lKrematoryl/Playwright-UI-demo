from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class FooterElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._footer = page.locator('#footer')

    @property
    def subscription_heading(self) -> Locator:
        return self._footer.get_by_role('heading', name='Subscription')

    @property
    def subscription_input(self) -> Locator:
        return self._footer.get_by_role('textbox', name='Your email address')

    @property
    def subscribe_button(self) -> Locator:
        return self._footer.get_by_role('button', name='Subscribe')

    @property
    def subscription_success_message(self) -> Locator:
        return self._footer.get_by_text('You have been successfully subscribed!')

    @property
    def copyright_text(self) -> Locator:
        return self._footer.get_by_text('Copyright © 2021 All rights reserved')
