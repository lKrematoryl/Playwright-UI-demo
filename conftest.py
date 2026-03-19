import pytest
from faker import Faker
from playwright.async_api import Page

from utils.page_builder import PageBuilder


@pytest.fixture
def _page_builder_instance(page: Page) -> PageBuilder: return PageBuilder(page)


@pytest.fixture(scope="session")
def _faker_instance() -> Faker: return Faker()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Fixture sets actual window size to 1920x1080 for the browser context.
    Required solely for debugging purposes
    """
    return {**browser_context_args,
            "viewport": {"width": 1920, "height": 1080},
            "screen": {"width": 1920, "height": 1080}}


@pytest.fixture(autouse=True)
def inject_pages(request: pytest.FixtureRequest, _page_builder_instance: PageBuilder):
    """
    Fixture injects page objects and page builder into the test class instance so it's not necessary to instantiate
    page object in every test.
    Pages are available in test cases via self. reference
    :param request:
    :param _page_builder_instance:
    :return:
    """
    if hasattr(request, 'cls') and request.cls is not None:
        request.cls.builder = _page_builder_instance
        request.cls.page = _page_builder_instance.page

        for attr_name in dir(_page_builder_instance):
            if not attr_name.startswith("_") and not attr_name.startswith("create_"):
                attr_value = getattr(_page_builder_instance, attr_name)
                if not callable(attr_value):
                    setattr(request.cls, attr_name, attr_value)


@pytest.fixture(autouse=True)
def inject_faker(request: pytest.FixtureRequest, _faker_instance: Faker) -> None:
    """
    Fixture injects faker instance into the test automatically. Faker instance is used for generating test data
    :param request:
    :param _faker_instance:
    :return:
    """
    cls = getattr(request, "cls", None)
    if cls and getattr(cls, "__faker_enabled__", True):
        cls.faker = _faker_instance
