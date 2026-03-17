from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class AdvertisementElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._advertisement = page.locator('section#advertisement')

    @property
    def banner_image(self) -> Locator:
        return self._advertisement.get_by_role('img')

    @property
    def search_input(self) -> Locator:
        return self._advertisement.get_by_role('textbox', name='Search Product')

    @property
    def search_button(self) -> Locator:
        return self._advertisement.get_by_role('button', name='Search')
