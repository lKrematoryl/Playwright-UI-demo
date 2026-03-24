from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class LoginFormElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('.login-form')

    @property
    def heading(self) -> Locator:
        return self._section.get_by_role('heading', name='Login to your account')

    @property
    def email_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Email Address')

    @property
    def password_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Password')

    @property
    def login_button(self) -> Locator:
        return self._section.get_by_role('button', name='Login')
