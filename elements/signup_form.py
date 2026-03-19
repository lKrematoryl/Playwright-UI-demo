from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class SignupFormElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('.signup-form')

    @property
    def heading(self) -> Locator:
        return self._section.get_by_role('heading', name='New User Signup!')

    @property
    def name_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Name')

    @property
    def email_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Email Address')

    @property
    def signup_button(self) -> Locator:
        return self._section.get_by_role('button', name='Signup')
