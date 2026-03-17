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
        return self._section.get_by_role('radio', name='Mr.')

    @property
    def title_mrs(self) -> Locator:
        return self._section.get_by_role('radio', name='Mrs.')

    @property
    def name_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Name')

    @property
    def email_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Email')

    @property
    def password_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Password')

    @property
    def day_select(self) -> Locator:
        return self._section.get_by_role('combobox', name='Day')

    @property
    def month_select(self) -> Locator:
        return self._section.get_by_role('combobox', name='Month')

    @property
    def year_select(self) -> Locator:
        return self._section.get_by_role('combobox', name='Year')

    @property
    def newsletter_checkbox(self) -> Locator:
        return self._section.get_by_role('checkbox', name='Sign up for our newsletter!')

    @property
    def optin_checkbox(self) -> Locator:
        return self._section.get_by_role('checkbox', name='Receive special offers from our partners!')

    # --- Address Information ---

    @property
    def address_heading(self) -> Locator:
        return self._section.get_by_role('heading', name='Address Information')

    @property
    def first_name_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='First name')

    @property
    def last_name_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Last name')

    @property
    def company_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Company')

    @property
    def address1_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Address')

    @property
    def address2_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Address 2')

    @property
    def country_select(self) -> Locator:
        return self._section.get_by_role('combobox', name='Country')

    @property
    def state_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='State')

    @property
    def city_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='City')

    @property
    def zipcode_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Zipcode')

    @property
    def mobile_number_input(self) -> Locator:
        return self._section.get_by_role('textbox', name='Mobile Number')

    @property
    def create_account_button(self) -> Locator:
        return self._section.get_by_role('button', name='Create Account')
