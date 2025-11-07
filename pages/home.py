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

    # menu bar section
    @property
    def menu_bar(self) -> "Locator":
        return ...

    @property
    def home_button(self) -> "Locator":
        return self.menu_bar.get_by_text('Home', exact=True)

    @property
    def search_button(self) -> "Locator":
        return self.menu_bar.get_by_text('Search', exact=True)

    @property
    def explore_button(self) -> "Locator":
        return self.menu_bar.get_by_text('Explore', exact=True)

    @property
    def reels_button(self) -> "Locator":
        return self.menu_bar.get_by_text('Reels', exact=True)

    @property
    def messages_button(self) -> "Locator":
        return self.menu_bar.get_by_text('Messages', exact=True)

    @property
    def notifications_button(self) -> "Locator":
        return self.menu_bar.get_by_text('Notifications', exact=True)

    @property
    def create_button(self) -> "Locator":
        return self.menu_bar.get_by_text('Create', exact=True)

    @property
    def profile_button(self) -> "Locator":
        return self.menu_bar.get_by_text('Profile', exact=True)

    ...

    # stories section
    @property
    def stories(self) -> "Locator":
        return self.page.locator('//div[@data-pagelet="story_tray"]').filter(has=self.page.get_by_role('list'))

    ...

    # articles section
    @property
    def article(self) -> "Locator":
        return self.page.get_by_role("article")

    @property
    def video(self):
        return self.article.locator('video')

    @property
    def like_button(self) -> "Locator":
        return self.article.get_by_label('Like')

    @property
    def commentary_button(self) -> "Locator":
        return self.article.get_by_label('Comment')

    @property
    def commentary_input(self) -> "Locator":
        return self.article.get_by_role("textbox", name="Add a comment…")

    @property
    def posted_commentary_text(self) -> "Locator":
        return self.page.get_by_role('heading', level=1)

    @property
    def post_button(self) -> "Locator":
        return self.article.get_by_role("button", name="Post")

    @property
    def share_button(self) -> "Locator":
        return self.article.get_by_label('Share')

    ...

    # suggested section
    @property
    def suggested(self) -> "Locator":
        return ...

    def open(self):
        super(BasePage).open()

    def like(self):
        self.like_button.click()

    def comment(self, comment: str):
        self.commentary_button.click()
        self.commentary_input.fill(comment)
        self.post_button.click()
