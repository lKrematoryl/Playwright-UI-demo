import os

from loguru import logger
from playwright.sync_api import Page, Locator

from pages.base_page import _BasePage


class _SignupPage(_BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    @property
    def url(self) -> str:
        return f"{os.getenv('BASE_URL')}/accounts/emailsignup/"

    @property
    def logo(self) -> "Locator":
        return self.page.get_by_label('Instagram')

    @property
    def welcome_text(self) -> "Locator":
        return self.page.get_by_role('heading', level=4, name='Sign up to see photos and videos from your friends.')

    @property
    def login_with_facebook_button(self) -> "Locator":
        return self.page.get_by_role('button', name='Log in with Facebook')

    @property
    def email_or_phone_input(self) -> "Locator":
        return self.page.locator('input[name="emailOrPhone"]')

    @property
    def incorrect_email_error_message(self) -> "Locator":
        return self.page.get_by_text('Enter a valid email address.')

    @property
    def incorrect_mobile_phone_error_message(self) -> "Locator":
        return self.page.get_by_text('Looks like your phone number may be incorrect. Please try entering your full '
                                     'number, including the country code.')

    @property
    def password_input(self) -> "Locator":
        return self.page.locator('input[name="password"]')

    @property
    def incorrect_password_error_message(self) -> "Locator":
        return self.page.get_by_text('Create a password that is at least 6 characters in length.')

    @property
    def full_name_input(self) -> "Locator":
        return self.page.locator('input[name="fullName"]')

    @property
    def username_input(self) -> "Locator":
        return self.page.locator('input[name="username"]')

    @property
    def username_taken_error_message(self) -> "Locator":
        return self.page.get_by_text("This username isn't available. Please try another.")

    @property
    def service_note_text(self) -> "Locator":
        return self.page.locator('span[style*="line-height"]:not([dir]):has(a)')

    @property
    def service_note_link(self) -> "Locator":
        return self.service_note_text.get_by_role('link')

    @property
    def terms_and_conditions_link(self) -> "Locator":
        return self.page.get_by_role('link', name='Terms')

    @property
    def privacy_policy_link(self) -> "Locator":
        return self.page.get_by_role('link', name='Privacy Policy')

    @property
    def cookies_policy_link(self) -> "Locator":
        return self.page.get_by_role('link', name='Cookies Policy')

    @property
    def sign_up_button(self) -> "Locator":
        return self.page.get_by_role('button', name='Sign up')

    @property
    def have_an_account_text(self) -> "Locator":
        return self.page.locator('p', has_text='Have an account?')

    @property
    def log_in_button(self) -> "Locator":
        return self.have_an_account_text.get_by_role('button')

    # Birthday modal
    @property
    def month(self) -> "Locator":
        return self.page.get_by_role('combobox', name='Month:')

    @property
    def day(self) -> "Locator":
        return self.page.get_by_role('combobox', name='Day:')

    @property
    def year(self) -> "Locator":
        return self.page.get_by_role('combobox', name='Year:')

    @property
    def next_button(self) -> "Locator":
        return self.page.get_by_role('button', name='Next')

    @property
    def go_back_button(self) -> "Locator":
        return self.page.get_by_role('button', name='Go back')

    @property
    def recaptcha_iframe(self) -> "Locator":
        return self.page.locator("#recaptcha-iframe")

    def register_user(self, email_or_mobile: str, password: str, full_name: str, username: str, month: str | int,
                      day: str | int, year: str | int) -> None:
        logger.info('Registering new user')
        logger.debug(f'Entering email or mobile phone: {email_or_mobile}')
        self.email_or_phone_input.fill(email_or_mobile)

        # not secure
        logger.debug(f'Entering password: {password}')
        self.password_input.fill(password)

        logger.debug(f'Entering full name: {full_name}')
        self.full_name_input.fill(full_name)

        logger.debug(f'Entering username: {username}')
        self.username_input.fill(username)
        self.sign_up_button.click()

        logger.info('Entering birth date')
        logger.debug(f'Selecting {month=}, {day=}, {year=}')
        self.month.select_option(str(month))
        self.day.select_option(str(day))
        self.year.select_option(str(year))
        self.next_button.click()
