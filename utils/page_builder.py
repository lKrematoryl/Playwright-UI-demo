from functools import cached_property
from typing import Iterator, Tuple

from playwright.async_api import Page

from pages.account_created import AccountCreatedPage
from pages.account_information_page import AccountInformationPage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_placed_page import OrderPlacedPage
from pages.payment_page import PaymentPage
from utils.custom_types import PageObject
from utils.element_builder import ElementBuilder


class PageBuilder:
    """
    This is a dedicated builder that allows to use pre-created page objects or create new ones on demand.
    Extend this builder when new page is added to the framework.
    - @cached_property is used for a lazy-load approach.
    - create_*page_name* methods create new page object instances. Use only when new instance of the same page is needed
    in the test.
    """

    def __init__(self, page: Page):
        self.page = page
        self._eb = ElementBuilder(self.page)

    def __dir__(self) -> list[str]:
        """
        Modified to return only page related attributes by filtering out non-related ones.
        E.g. will return 'login_page', 'create_login_page' but skips __class__, etc.
            :return: List of page related attribute names.
        """
        return [name for name in super().__dir__() if name.endswith("_page")]

    def __iter__(self) -> Iterator[Tuple[str, PageObject]]:
        """
        Iteration happens only via page related attributes.
        """
        for name in self.__dir__():
            yield name, getattr(self, name)

    @cached_property
    def home_page(self) -> HomePage:
        return HomePage(self.page, self._eb)

    def create_home_page(self) -> HomePage:
        """ Creates a new instance of HomePage """
        return HomePage(self.page, self._eb)

    @cached_property
    def login_page(self) -> LoginPage:
        return LoginPage(self.page, self._eb)

    def create_login_page(self) -> LoginPage:
        """ Creates a new instance of LoginPage """
        return LoginPage(self.page, self._eb)

    @cached_property
    def account_information_page(self) -> AccountInformationPage:
        return AccountInformationPage(self.page, self._eb)

    def create_account_information_page(self) -> AccountInformationPage:
        """ Creates a new instance of AccountInformationPage """
        return AccountInformationPage(self.page, self._eb)

    @cached_property
    def cart_page(self) -> CartPage:
        return CartPage(self.page, self._eb)

    def create_cart_page(self) -> CartPage:
        """ Creates a new instance of CartPage """
        return CartPage(self.page, self._eb)

    @cached_property
    def payment_page(self) -> PaymentPage:
        return PaymentPage(self.page, self._eb)

    def create_payment_page(self) -> PaymentPage:
        """ Creates a new instance of PaymentPage """
        return PaymentPage(self.page, self._eb)

    @cached_property
    def order_placed_page(self) -> OrderPlacedPage:
        return OrderPlacedPage(self.page, self._eb)

    def create_order_placed_page(self) -> OrderPlacedPage:
        """ Creates a new instance of OrderPlacedPage """
        return OrderPlacedPage(self.page, self._eb)

    @cached_property
    def account_created_page(self):
        return AccountCreatedPage(self.page, self._eb)

    def create_account_created_page(self) -> AccountCreatedPage:
        """ Creates a new instance of AccountCreatedPage """
        return AccountCreatedPage(self.page, self._eb)
