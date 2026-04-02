from playwright.async_api import Page

from pages.base_page import BasePage
from utils.element_builder import ElementBuilder


class AccountCreatedPage(BasePage):

    def __init__(self, page: Page, element_builder: ElementBuilder):
        super().__init__(page)
        self.header = element_builder.header
        self.footer = element_builder.footer
        self.account_created = element_builder.create_account_created()

    @property
    def url(self) -> str:
        return f'{super(BasePage).url}/account_created'

    async def continue_to_home(self):
        await self.account_created.continue_button.click()
