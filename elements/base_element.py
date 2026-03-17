from abc import ABC
from playwright.async_api import Page


class _BaseElement(ABC):
    def __init__(self, page: Page):
        self.page = page
