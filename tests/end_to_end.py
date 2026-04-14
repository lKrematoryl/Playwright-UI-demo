import pytest
from playwright.async_api import expect

from .base_test import BaseTest


class TestEndToEnd(BaseTest):

    @pytest.mark.usefixtures("open_home_page", "delete_account_after_test")
    async def test_register_user(self):
        user = self.test_data.valid_user
        await self.home_page.header.signup_login_link.click(force=True)
        await self.login_page.signup(username=user.username, email=user.email)
        await self.account_information_page.register_user(data=user)
        await self.account_created_page.continue_to_home()

        await expect(self.home_page.header.logged_in_as,
                     "User should be logged in after account creation").to_be_visible()
        await expect(self.home_page.header.logged_in_as,
                     f"Logged in username should be '{user.username}'").to_contain_text(user.username)

    async def test_login_user_valid(self, register_user_and_logout, delete_account_after_test):
        user = register_user_and_logout
        await self.home_page.header.signup_login_link.click(force=True)
        await self.login_page.login(email=user.email, password=user.password)

        await expect(self.home_page.header.logged_in_as,
                     f"Logged in username should be '{user.username}'").to_contain_text(user.username)

    @pytest.mark.usefixtures("open_home_page")
    async def test_login_user_invalid(self):
        user = self.test_data.invalid_user
        await self.login_page.open()
        await self.login_page.login(email=user.email, password=user.password)

        await expect(self.login_page.login_form.error_message,
                     "Error message isn't displayed after login with incorrect credentials").to_be_visible()
