# Playwright UI Automation Framework

Async Playwright + Pytest framework for end-to-end UI testing against **[automationexercise.com](https://automationexercise.com/)**.

## Architecture

The framework follows a **three-layer architecture** separating locators, page logic, and test orchestration:

```
├── elements/          # Layer 1: Locator wrappers (UI components)
│   ├── base_element.py
│   ├── auth/          # Login, Signup, Registration, Account Created
│   ├── cart/          # Empty cart, Filled cart
│   ├── checkout/      # Address details, Order review, Order comment
│   ├── contact/       # Contact Us form
│   ├── home/          # Slider, Features items, Recommended items
│   ├── modals/        # Checkout modal
│   ├── payment/       # Payment form, Order placed
│   ├── products/      # Product card, Advertisement
│   └── shared/        # Header, Footer, Breadcrumb, Left sidebar
│
├── pages/             # Layer 2: Page Objects (compose elements + actions)
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── account_information_page.py
│   ├── account_created_page.py
│   ├── cart_page.py
│   ├── payment_page.py
│   └── order_placed_page.py
│
├── tests/             # Layer 3: Test suites and preconditions
│   ├── preconditions.py
│   └── end_to_end.py
│
├── utils/             # Builders, models, helpers
│   ├── element_builder.py
│   ├── page_builder.py
│   ├── data_builder.py
│   ├── models.py
│   └── custom_types.py
│
├── conftest.py        # Fixtures: page injection, faker, ad-blocking, timeouts
├── pytest.ini         # Pytest and Playwright configuration
├── .env               # Environment variables (BASE_URL, credentials)
└── requirements.txt   # Dependencies
```

## Design Patterns

### Builder Pattern

The framework uses dedicated builders for each layer:

- **`ElementBuilder`** — creates element instances. Shared elements (header, footer, sidebar, breadcrumb) use `@cached_property` for single-instance-per-test. Page-specific elements use `create_*()` factory methods.
- **`PageBuilder`** — creates page objects. Same lazy-load approach with `@cached_property` and `create_*()` escape hatches when a fresh instance is needed.
- **`DataBuilder`** — creates test data objects. Provides `valid_user`, `invalid_user` properties and a `custom_user()` method for overrides.

### Automatic Fixture Injection

Page objects and test data are injected into test classes automatically via `conftest.py` fixtures. No manual instantiation needed — access everything through `self`:

```python
class TestEndToEnd(HomePageNotLoggedIn):

    async def test_register_user(self):
        user = self.data.valid_user
        await self.home_page.header.signup_login_link.click()
        await self.login_page.signup(username=user.username, email=user.email)
        await self.account_information_page.register_user(data=user)
```

### Precondition Classes

Test setup is handled through inheritance. Precondition classes define `autouse` fixtures that prepare the required state:

```python
class HomePageNotLoggedIn(_BaseTest):
    @pytest.fixture(autouse=True)
    async def open_home_page(self, inject_pages):
        await self.home_page.open()

class TestSomething(HomePageNotLoggedIn):
    # home page is already open when test starts
    async def test_example(self):
        ...
```

### Test Data Models

Test data is managed through dataclasses with factory methods:

```python
# Random valid user
user = self.data.valid_user

# Random invalid user
user = self.data.invalid_user

# Custom overrides
user = self.data.custom_user(title='Mrs', country='Canada')
```

## Setup

### Prerequisites

- Python 3.13+
- pip

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd playwright_ui_demo

# Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Configuration

Environment variables in `.env`:

```
BASE_URL="https://automationexercise.com/"
USERNAME="your_username"
PASSWORD="your_password"
```

Browser settings in `pytest.ini`:

```ini
playwright_browser = chromium
playwright_headed = True
playwright_timeout = 10000
```

## Running Tests

```bash
# Run all tests (headed)
pytest

# Run headless
pytest --headed=false

# Run specific test file
pytest tests/end_to_end.py

# Run specific test
pytest tests/end_to_end.py::TestEndToEnd::test_register_user

# Run with verbose output
pytest -v
```

## Extending the Framework

### Adding a New Page

1. Create element classes in `elements/<domain>/`
2. Register elements in `ElementBuilder` (`utils/element_builder.py`)
3. Create page class in `pages/`
4. Register page in `PageBuilder` (`utils/page_builder.py`)
5. Add type hint to `_BaseTest` in `tests/preconditions.py`

### Adding Test Data

1. Create a dataclass with `valid`/`invalid` factory methods in `utils/models.py`
2. Add a property/method to `DataBuilder` in `utils/data_builder.py`

## Stack

- **Python 3.13+**
- **Playwright** — browser automation
- **Pytest** — test runner
- **pytest-playwright** — Playwright integration for pytest
- **Faker** — test data generation
- **Loguru** — logging
