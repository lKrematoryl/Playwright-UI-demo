from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class BreadcrumbElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._breadcrumb = page.locator('div.breadcrumbs')

    @property
    def home_link(self) -> Locator:
        return self._breadcrumb.get_by_role('link', name='Home')

    @property
    def active_item(self) -> Locator:
        return self._breadcrumb.get_by_role('listitem').last
