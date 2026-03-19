from playwright.async_api import Page

from pages.base_page import _BasePage
from utils.element_builder import ElementBuilder


class PaymentPage(_BasePage):

    def __init__(self, page: Page, element_builder: ElementBuilder):
        super().__init__(page)
        self.header = element_builder.header
        self.footer = element_builder.footer
        self.breadcrumb = element_builder.breadcrumb
        self.payment_form = element_builder.create_payment_form()

    @property
    def url(self) -> str:
        return f'{super(_BasePage).url}/payment'
