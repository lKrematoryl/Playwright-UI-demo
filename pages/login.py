import os

from loguru import logger
from playwright.async_api import Page, Locator

from pages.base_page import _BasePage
from utils.element_builder import ElementBuilder


class LoginPage(_BasePage):

    def __init__(self, page: Page, element_builder: ElementBuilder):
        super().__init__(page)
        self.header = element_builder.header
        self.footer = element_builder.footer
        self.login_form = element_builder.create_login_form()
        self.signup_form = element_builder.create_signup_form()

    @property
    def url(self) -> str:
        return f"{os.getenv('BASE_URL')}/login"

    async def login(self, username: str, password: str) -> None:
        logger.info(f"Logging in with username: {username}")
        logger.debug(f'Entering {username=} and {password=}')
        await self.login_form.email_input.fill(username)
        await self.login_form.password_input.fill(password)
        await self.login_form.login_button.click()
