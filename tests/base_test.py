from dataclasses import dataclass

import pytest
from faker import Faker
from playwright.async_api import Page

from pages.account_created import AccountCreatedPage
from pages.account_information_page import AccountInformationPage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_placed_page import OrderPlacedPage
from pages.payment_page import PaymentPage
from utils.data_builder import DataBuilder
from utils.page_builder import PageBuilder


@pytest.mark.usefixtures("inject_pages")
@dataclass(init=False, eq=False)
class BaseTest:
    """
    This class is required to tell the IDE that test class, that inherits from it, will have these attributes.
    Excluded from initialization as used as type hinting only. Each new element must be listed in this class.
    - frozen=True will prevent fixture injection, don't set
    - eq=False to avoid unhashable type error in pytest
    """
    builder: PageBuilder
    page: Page
    faker: Faker
    test_data: DataBuilder

    login_page: LoginPage
    home_page: HomePage
    cart_page: CartPage
    account_information_page: AccountInformationPage
    order_placed_page: OrderPlacedPage
    payment_page: PaymentPage
    account_created_page: AccountCreatedPage
