from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class AccountRegistrationElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('section#form')

    # --- Account Information ---

    @property
    def heading(self) -> Locator:
        return self._section.get_by_role('heading', name='Enter Account Information')

    @property
    def title_mr(self) -> Locator:
        return self._section.locator('#id_gender1')

    @property
    def title_mrs(self) -> Locator:
        return self._section.locator('#id_gender2')

    @property
    def name_input(self) -> Locator:
        return self._section.locator('[data-qa="name"]')

    @property
    def email_input(self) -> Locator:
        return self._section.locator('[data-qa="email"]')

    @property
    def password_input(self) -> Locator:
        return self._section.locator('[data-qa="password"]')

    @property
    def day_select(self) -> Locator:
        return self._section.locator('[data-qa="days"]')

    @property
    def month_select(self) -> Locator:
        return self._section.locator('[data-qa="months"]')

    @property
    def year_select(self) -> Locator:
        return self._section.locator('[data-qa="years"]')

    @property
    def newsletter_checkbox(self) -> Locator:
        return self._section.locator('#newsletter')

    @property
    def optin_checkbox(self) -> Locator:
        return self._section.locator('#optin')

    # --- Address Information ---

    @property
    def address_heading(self) -> Locator:
        return self._section.get_by_role('heading', name='Address Information')

    @property
    def first_name_input(self) -> Locator:
        return self._section.locator('[data-qa="first_name"]')

    @property
    def last_name_input(self) -> Locator:
        return self._section.locator('[data-qa="last_name"]')

    @property
    def company_input(self) -> Locator:
        return self._section.locator('[data-qa="company"]')

    @property
    def address1_input(self) -> Locator:
        return self._section.locator('[data-qa="address"]')

    @property
    def address2_input(self) -> Locator:
        return self._section.locator('[data-qa="address2"]')

    @property
    def country_select(self) -> Locator:
        return self._section.locator('[data-qa="country"]')

    @property
    def state_input(self) -> Locator:
        return self._section.locator('[data-qa="state"]')

    @property
    def city_input(self) -> Locator:
        return self._section.locator('[data-qa="city"]')

    @property
    def zipcode_input(self) -> Locator:
        return self._section.locator('[data-qa="zipcode"]')

    @property
    def mobile_number_input(self) -> Locator:
        return self._section.locator('[data-qa="mobile_number"]')

    @property
    def create_account_button(self) -> Locator:
        return self._section.locator('[data-qa="create-account"]')

