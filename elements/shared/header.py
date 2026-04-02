from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class HeaderElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._header = page.locator('header')

    @property
    def logo(self) -> Locator:
        return self._header.get_by_role('link', name='Website for automation practice')

    @property
    def logo_image(self) -> Locator:
        return self.logo.get_by_role('img')

    @property
    def navbar(self) -> Locator:
        return self._header.get_by_role('navigation')

    @property
    def home_link(self) -> Locator:
        return self._header.get_by_role('link', name='Home', exact=True)

    @property
    def products_link(self) -> Locator:
        return self._header.get_by_role('link', name='Products', exact=True)

    @property
    def cart_link(self) -> Locator:
        return self._header.get_by_role('link', name='Cart', exact=True)

    @property
    def signup_login_link(self) -> Locator:
        return self._header.locator("a[href='/login']")

    @property
    def logout_link(self) -> Locator:
        return self._header.get_by_role('link', name='Logout', exact=True)

    @property
    def delete_account_link(self) -> Locator:
        return self._header.get_by_role('link', name='Delete Account', exact=True)

    @property
    def logged_in_as(self) -> Locator:
        return self._header.get_by_text('Logged in as', exact=False)

    @property
    def test_cases_link(self) -> Locator:
        return self._header.get_by_role('link', name='Test Cases', exact=True)

    @property
    def api_testing_link(self) -> Locator:
        return self._header.get_by_role('link', name='API Testing', exact=True)

    @property
    def video_tutorials_link(self) -> Locator:
        return self._header.get_by_role('link', name='Video Tutorials', exact=True)

    @property
    def contact_us_link(self) -> Locator:
        return self._header.get_by_role('link', name='Contact us', exact=True)
