from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class AccountCreatedElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('section#form')

    @property
    def heading(self) -> Locator:
        return self._section.get_by_role('heading', name='Account Created!')

    @property
    def congratulations_text(self) -> Locator:
        return self._section.get_by_text('Congratulations! Your new account has been successfully created!')

    @property
    def member_privileges_text(self) -> Locator:
        return self._section.get_by_text('You can now take advantage of member privileges to enhance your online '
                                         'shopping experience with us.')

    @property
    def continue_button(self) -> Locator:
        return self._section.get_by_role('link', name='Continue')
