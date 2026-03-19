from playwright.async_api import Page

from pages.base_page import _BasePage
from utils.element_builder import ElementBuilder


class CartPage(_BasePage):

    def __init__(self, page: Page, element_builder: ElementBuilder):
        super().__init__(page)
        self.header = element_builder.header
        self.footer = element_builder.footer
        self.breadcrumb = element_builder.breadcrumb
        self.cart_empty = element_builder.create_cart_empty()
        self.cart_filled = element_builder.create_cart_filled()
        self.checkout_modal = element_builder.create_checkout_modal()

    @property
    def url(self) -> str:
        return f'{super(_BasePage).url}/view_cart'
