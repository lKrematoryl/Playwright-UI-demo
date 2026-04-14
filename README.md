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
├── tests/             # Layer 3: Test suites
│   ├── conftest.py    # Test fixtures: preconditions and postconditions
│   ├── base_test.py   # Type hints for fixture-injected attributes
│   └── end_to_end.py
│
├── utils/             # Builders, models, helpers
│   ├── element_builder.py
│   ├── page_builder.py
│   ├── data_builder.py
│   ├── models.py
│   └── custom_types.py
│
├── conftest.py        # Root fixtures: browser config, injection, timeouts
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

Page objects and test data are injected into test classes automatically via root `conftest.py` fixtures. No manual instantiation needed — access everything through `self`:

```python
class TestEndToEnd(BaseTest):

    async def test_example(self, open_home_page):
        await self.home_page.header.products_link.click()
```

`BaseTest` provides type hints for all injected attributes, giving full IDE autocomplete with zero behavioral logic.

### Composable Preconditions and Postconditions

Test setup and teardown is handled through **composable fixtures** defined in `tests/conftest.py`. Each test requests only the fixtures it needs — no rigid inheritance hierarchies:

```python
class TestEndToEnd(BaseTest):

    # test that only needs the home page open
    async def test_register_user(self, open_home_page):
        ...

    # test that needs a registered user (includes open_home_page as dependency)
    async def test_delete_user(self, register_and_delete_user):
        ...

    # test that needs a registered + logged out user
    async def test_login(self, register_user_and_logout):
        ...
```

Fixtures chain together via dependencies:

```
open_home_page
    └── register_user (depends on open_home_page)
            ├── register_and_delete_user (setup + teardown)
            └── register_user_and_logout (setup + logout)
```

Precondition fixtures that create test data yield it back to the test:

```python
async def test_login(self, register_user_and_logout):
    user = register_user_and_logout  # RegistrationData object
    await self.login_page.login(email=user.email, password=user.password)
```

### Two-Level Conftest

- **Root `conftest.py`** — framework infrastructure: browser configuration, ad-blocking, timeout defaults, automatic injection of page objects, faker, and data builder.
- **`tests/conftest.py`** — test-specific fixtures: preconditions (open page, register user), postconditions (delete account), and composed workflows.

### Test Data Models

Test data is managed through dataclasses with factory methods, accessed via `DataBuilder`:

```python
# Random valid user
user = self.test_data.valid_user

# Random invalid user
user = self.test_data.invalid_user

# Custom overrides
user = self.test_data.custom_user(title='Mrs', country='Canada')
```

Each access generates fresh random data via Faker. The `DataBuilder` is injected once per test — it's a factory, not stored data.

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
5. Add type hint to `BaseTest` in `tests/base_test.py`

### Adding Test Data

1. Create a dataclass with `valid`/`invalid` factory methods in `utils/models.py`
2. Add a property/method to `DataBuilder` in `utils/data_builder.py`

### Adding Preconditions/Postconditions

1. Create a fixture in `tests/conftest.py`
2. Chain it with existing fixtures via dependencies
3. Use `yield` for postcondition (teardown) logic
4. Tests request the fixture by name via argument or `@pytest.mark.usefixtures`

## Stack

- **Python 3.13+**
- **Playwright** — browser automation
- **Pytest** — test runner
- **pytest-playwright** — Playwright integration for pytest
- **Faker** — test data generation
- **Loguru** — logging
