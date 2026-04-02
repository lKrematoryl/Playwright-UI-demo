from playwright.async_api import Page

from pages.base_page import BasePage
from utils.element_builder import ElementBuilder


class HomePage(BasePage):

    def __init__(self, page: Page, element_builder: ElementBuilder):
        super().__init__(page)
        self.header = element_builder.header
        self.footer = element_builder.footer
        self.slider = element_builder.create_slider()
        self.sidebar = element_builder.left_sidebar
        self.features_items = element_builder.create_features_items()
        self.recommended_items = element_builder.create_recommended_items()

    @property
    def url(self) -> str:
        return super().url

    async def open(self):
        await self.page.goto(self.url, wait_until="domcontentloaded")
