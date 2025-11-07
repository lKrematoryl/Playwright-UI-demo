from dataclasses import dataclass

import pytest
from faker import Faker
from playwright.sync_api import Page

from pages import SignupPage, LoginPage, HomePageLoggedIn, HomePageNotLoggedIn
from utils.page_builder import _Pagebuilder


@pytest.mark.usefixtures("inject_pages")
@dataclass(init=False, eq=False)
class _BaseTest:
    """
    This class is required to tell the IDE that test class, that inherits from it, will have these attributes.
    Excluded from initialization as used as type hinting only. Each new element must be listed in this class.
    - frozen=True will prevent fixture injection, don't set
    - eq=False to avoid unhashable type error in pytest
    """
    builder: _Pagebuilder
    page: Page
    faker: Faker

    signup_page: SignupPage
    login_page: LoginPage
    home_page_not_logged: HomePageNotLoggedIn
    home_page_logged: HomePageLoggedIn


# Here precondition classes can be defined that will prepare required setup for tests. E.g. use fixtures for
# opening page, registering user, logging in, etc. Each precondition class must inherit from _BaseTest
class GenericSetup(_BaseTest):
    pass


class SignupPageNotRegisteredUser(_BaseTest):

    @classmethod
    def setup_method(cls):
        cls.signup_page.open()


class LoginPageNotLoggedIn(_BaseTest):

    @classmethod
    def setup_method(cls):
        cls.login_page.open()


class HomePageNotLogged(_BaseTest):

    @classmethod
    def setup_method(cls):
        cls.home_page_not_logged.open()


class HomePageLogged(_BaseTest):

    @classmethod
    def setup_method(cls):
        cls.home_page_not_logged.open()
