import os

from loguru import logger
from playwright.sync_api import Page, Locator

from pages.base_page import _BasePage


class _LoginPage(_BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    @property
    def url(self) -> str:
        return f"{os.getenv('BASE_URL')}/accounts/login/"

    @property
    def login_form(self):
        return ...

    @property
    def logo(self) -> "Locator":
        return self.page.get_by_label('Instagram')

    @property
    def username_input(self) -> "Locator":
        return self.page.locator('input[name="username"]')

    @property
    def password_input(self) -> "Locator":
        return self.page.locator('input[name="password"]')

    @property
    def login_button(self) -> "Locator":
        return self.page.get_by_role('button', name='Log in', exact=True)

    @property
    def login_with_facebook_button(self) -> "Locator":
        return self.page.locator('button:has-text("Log in with Facebook")')

    @property
    def facebook_image(self) -> "Locator":
        return self.login_with_facebook_button.get_by_role('img', name='Log in with Facebook')

    @property
    def log_in_with_facebook_text(self) -> "Locator":
        return self.login_with_facebook_button.locator("span", has_text='Log in with Facebook')

    @property
    def forgot_password_link(self) -> "Locator":
        return self.page.get_by_role('link', name='Forgotten your password?')

    @property
    def signup_prompt_paragraph(self) -> "Locator":
        return self.page.locator("p", has_text="Don't have an account?")

    @property
    def sign_up_link(self) -> "Locator":
        return self.page.get_by_role('link', name='Sign up')

    @property
    def recaptcha_iframe(self) -> "Locator":
        return self.page.locator("#recaptcha-iframe")

    def login(self, username: str, password: str) -> None:
        logger.info(f"Logging in with username: {username}")
        logger.debug(f'Entering {username=} and {password=}')
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
