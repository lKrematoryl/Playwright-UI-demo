import pytest

from playwright.async_api import Error as PlaywrightError


@pytest.fixture
async def open_home_page(request, _page_builder_instance):
    """Opens the home page before test execution."""
    await request.cls.home_page.open()


@pytest.fixture
async def register_user(request, open_home_page):
    """
    Registers a new user before test execution.
    User credentials are available via self.user attribute.
    After execution, user is logged in and on the home page.
    """
    cls = request.cls
    user = cls.test_data.valid_user
    await cls.home_page.header.signup_login_link.click(force=True)
    await cls.login_page.signup(username=user.username, email=user.email)
    await cls.account_information_page.register_user(data=user)
    await cls.account_created_page.continue_to_home()
    yield user


@pytest.fixture
async def register_and_delete_user(request, register_user):
    """
    Registers a new user before test execution.
    User credentials are available via self.user attribute.
    After execution, user is logged in and on the home page.
    User is deleted after the test completes.
    """
    yield register_user
    try:
        await request.cls.home_page.header.delete_account_link.click(force=True)
    except PlaywrightError:
        pass


@pytest.fixture
async def register_user_and_logout(request, register_user):
    """
    Registers a new user, then logs out.
    User credentials are available via self.user attribute.
    After execution, user is logged out and on the home page.
    """
    await request.cls.home_page.header.logout_link.click()
    await request.cls.home_page.open()
    yield register_user


@pytest.fixture
async def delete_account_after_test(request):
    yield
    try:
        await request.cls.home_page.header.delete_account_link.click(force=True)
    except PlaywrightError:
        pass
