from playwright.async_api import Page

from pages.base_page import BasePage
from utils.element_builder import ElementBuilder


class OrderPlacedPage(BasePage):

    def __init__(self, page: Page, element_builder: ElementBuilder):
        super().__init__(page)
        self.header = element_builder.header
        self.footer = element_builder.footer
        self.order_placed = element_builder.create_order_placed()

    @property
    def url(self) -> str:
        return f'{super(BasePage).url}/payment_done'

    async def open(self):
        await self.page.goto(self.url)
