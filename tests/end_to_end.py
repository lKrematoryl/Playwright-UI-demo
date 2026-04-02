import pytest
from playwright.async_api import Error as PlaywrightError
from playwright.async_api import expect

from .preconditions import HomePageNotLoggedIn


class TestEndToEnd(HomePageNotLoggedIn):

    @pytest.fixture
    async def delete_account_after_test(self):
        yield
        try:
            await self.home_page.header.delete_account_link.click(force=True)
        except PlaywrightError:
            pass

    async def test_register_user(self, delete_account_after_test):
        user = self.data.valid_user
        await self.home_page.header.signup_login_link.click(force=True)
        await self.login_page.signup(username=user.username, email=user.email)
        await self.account_information_page.register_user(data=user)

        await expect(self.account_created_page.account_created.heading,
                     "Account Created heading should be displayed after registration").to_be_visible()
        await self.account_created_page.continue_to_home()

        await expect(self.home_page.header.logged_in_as,
                     "User should be logged in after account creation").to_be_visible()
        await expect(self.home_page.header.logged_in_as,
                     f"Logged in username should be '{user.username}'").to_contain_text(user.username)
