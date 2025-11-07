from playwright.sync_api import Page, Locator


class _GetTheAppElements:
    def __init__(self, page: Page):
        self.page = page

    @property
    def get_the_app_text(self) -> "Locator":
        return self.page.locator("span", has_text="Get the app.")

    @property
    def google_store_badge(self) -> "Locator":
        return self.page.get_by_role('link', name='Get it on Google Play')

    @property
    def google_store_badge_img(self) -> "Locator":
        return self.google_store_badge.get_by_role('img')

    @property
    def microsoft_store_badge(self) -> "Locator":
        return self.page.get_by_role('link', name='Get it from Microsoft')

    @property
    def microsoft_store_badge_img(self) -> "Locator":
        return self.microsoft_store_badge.get_by_role('img')


class _FooterElements:
    def __init__(self, page: Page):
        self.page = page
