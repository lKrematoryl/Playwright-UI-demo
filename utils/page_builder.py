from functools import cached_property
from typing import Iterator, Tuple

from pages import SignupPage, LoginPage, HomePageLoggedIn, HomePageNotLoggedIn
from utils.custom_types import PageObject
from utils.element_builder import ElementBuilder


class _Pagebuilder:
    """
    This is a dedicated builder that allows to use pre-created page objects or create new ones on demand.
    Extend this builder when new page is added to the framework.
    - @cached_property is used for a lazy-load approach.
    - creat_*page_name* methods create new page object instances. Use only when new instance of the same page is needed
    in the test.
    """

    def __init__(self, page):
        self.page = page
        self._element_builder = ElementBuilder(self.page)

    def __dir__(self) -> list['str']:
        """
        Modified to return only page related attributes by filtering out non-related ones.
        E.g. will return 'signup_page', 'create_signup_page' but skips __class__, create_builder, etc.
            :return: List of page related attribute names.
        """
        return [name for name in super().__dir__() if name.endswith("_page")]

    def __iter__(self) -> Iterator[Tuple[str, PageObject]]:
        """
        Modifies that iteration happens only via page related attributes.
        """
        for name in self.__dir__():
            yield name, getattr(self, name)

    @cached_property
    def signup_page(self) -> SignupPage:
        return SignupPage(self.page)

    def create_signup_page(self) -> SignupPage:
        """ Creates a new instance of SignupPage """
        return SignupPage(self.page)

    @cached_property
    def login_page(self) -> PageObject:
        return LoginPage(self.page)

    def create_login_page(self) -> PageObject:
        """ Creates a new instance of LoginPage """
        return LoginPage(self.page)

    @cached_property
    def home_page_not_logged(self) -> PageObject:
        return HomePageNotLoggedIn(self.page)

    def create_home_page_not_logged(self) -> PageObject:
        """ Creates a new instance of HomePage for not logged-in user """
        return HomePageNotLoggedIn(self.page)

    @cached_property
    def home_page_logged(self) -> PageObject:
        return HomePageLoggedIn(self.page)

    def create_home_page_logged(self) -> PageObject:
        """ Creates a new instance of HomePage for logged-in user """
        return HomePageLoggedIn(self.page)
