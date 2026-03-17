from playwright.sync_api import Locator

from pages import LoginPage, BasePage


class _HomePageNotLoggedIn(BasePage, LoginPage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    @property
    def url(self) -> str:
        return super(BasePage).url

    @property
    def brand_landing(self) -> "Locator":
        return self.page.get_by_role("img").filter(has=self.page.locator("img[src*='landing-3x.png']"))

    def open(self):
        super(BasePage).open()


class _HomePageLoggedIn(BasePage):
    """
    This class represents the home page of a web application when a user is logged in.
    It's an approximate description of the class. Some elements or group of elements should be grouped into separate
    components and be described accordingly
    """

    # TODO: WIP: Decompose PageObjects into smaller PageElements
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    @property
    def url(self) -> str:
        return super(BasePage).url

    def open(self):
        super(BasePage).open()

    def like(self):
        self.like_button.click()

    def comment(self, comment: str):
        self.commentary_button.click()
        self.commentary_input.fill(comment)
        self.post_button.click()
