from abc import ABC, abstractmethod


class _BasePage(ABC):
    """
    Base class that define common structure for all page objects.
    """

    def __init__(self, page):
        self.page = page

    @property
    @abstractmethod
    def url(self) -> str:
        pass

    async def open(self):
        await self.page.goto(self.url)
