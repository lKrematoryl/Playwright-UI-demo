from playwright.sync_api import expect

from tests.preconditions import HomePageNotLogged, HomePageLogged


class TestHomePageNotLoggedIn(HomePageNotLogged):
    """
    This test suite contains tests related to the test scenario when not logged in user opens the home page.
    """

    def test_not_logged_user_on_login_page(self):
        """
        Test verifies that not logged user is redirected to a login page
        """
        expect(self.home_page_not_logged.login_form, message='Login form is not displayed').to_be_visible()

    def test_brand_landing_present(self):
        """
        Test verifies that brand landing image is present on the home page for not logged in users.
        """
        expect(self.home_page_not_logged.brand_landing, message='Brand landing is not present on the home page '
                                                                'for not logged in user').to_be_visible()


class TestHomePageLoggedIn(HomePageLogged):
    def test_home_page_structure(self):
        """
        This test case verifies the structure of the menu bar section
        """
        expect(self.home_page_logged.menu_bar, message=f"Actual menu bar structure doesn't match the shanpshot"
               ).to_match_aria_snapshot('tests/snapshots/home_page_logged_in/menu_bar.yaml')

    def test_comment_a_post(self):
        """
        This test case verifies that user can leave a commentary on a post.
        """
        commentary_text = 'test'
        self.home_page_logged.comment(commentary_text)
        expect(self.home_page_logged.posted_commentary_text,
               message=f'Expected commentary with the {commentary_text=} was not posted').to_have_text(commentary_text)
