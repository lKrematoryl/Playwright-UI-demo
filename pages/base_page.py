import os
from abc import ABC, abstractmethod


class BasePage(ABC):
    """
    Base class that define common structure for all page objects.
    """

    def __init__(self, page):
        self.page = page

    @property
    @abstractmethod
    def url(self) -> str:
        return os.getenv("BASE_URL")

    async def open(self):
        pass
