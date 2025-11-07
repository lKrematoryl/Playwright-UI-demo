from playwright.sync_api import expect

from tests.preconditions import LoginPageNotLoggedIn


class TestLoginPageNotLoggedIn(LoginPageNotLoggedIn):

    def test_login_unregistered_user(self):
        """
        Test verifies that unregistered user cannot log in via login page.

        Note:
            Currently test ends on recaptcha presence verification
        """
        self.login_page.login(username='TEST', password='TEST1234')
        expect(self.login_page.recaptcha_iframe, message='User logged in successfully').to_be_visible()

    def test_login_with_facebook(self):
        """
        Test verifies that user is redirected to Facebook login page after click on dedicated link
        """
        self.login_page.login_with_facebook_button.click()
        expect(self.page.locator("html")).to_have_attribute("id", "facebook")

    def test_login_form_snapshot(self):
        """
        Test verifies structure of the login form modal

        Note:
            This is just a dummy test to showcase aria snapshot feature
        :return:
        """
        expect(self.login_page.login_form).to_match_aria_snapshot(path='tests/snapshots/login_modal.yaml')
