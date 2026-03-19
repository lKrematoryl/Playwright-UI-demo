from loguru import logger
from playwright.async_api import Page

from pages.base_page import _BasePage
from utils.element_builder import ElementBuilder


class AccountInformationPage(_BasePage):

    def __init__(self, page: Page, element_builder: ElementBuilder):
        super().__init__(page)
        self.header = element_builder.header
        self.footer = element_builder.footer
        self.account_registration = element_builder.create_account_registration()

    @property
    def url(self) -> str:
        return f'{super(_BasePage).url}/signup'

    async def register_user(self, title: str, name: str, password: str, day: str | int, month: str | int,
                            year: str | int, first_name: str, last_name: str, company: str, address1: str,
                            address2: str, country: str, state: str, city: str, zipcode: str,
                            mobile_number: str) -> None:
        logger.info('Registering new user')

        logger.debug(f'Selecting title: {title}')
        if title == 'Mr':
            await self.account_registration.title_mr.check()
        else:
            await self.account_registration.title_mrs.check()

        logger.debug(f'Entering name: {name}')
        await self.account_registration.name_input.fill(name)

        logger.debug(f'Entering password: {password}')
        await self.account_registration.password_input.fill(password)

        logger.debug(f'Selecting day: {day}, month: {month}, year: {year}')
        await self.account_registration.day_select.select_option(str(day))
        await self.account_registration.month_select.select_option(str(month))
        await self.account_registration.year_select.select_option(str(year))

        logger.debug(f'Entering first name: {first_name}')
        await self.account_registration.first_name_input.fill(first_name)

        logger.debug(f'Entering last name: {last_name}')
        await self.account_registration.last_name_input.fill(last_name)

        logger.debug(f'Entering company: {company}')
        await self.account_registration.company_input.fill(company)

        logger.debug(f'Entering address1: {address1}')
        await self.account_registration.address1_input.fill(address1)

        logger.debug(f'Entering address2: {address2}')
        await self.account_registration.address2_input.fill(address2)

        logger.debug(f'Selecting country: {country}')
        await self.account_registration.country_select.select_option(country)

        logger.debug(f'Entering state: {state}')
        await self.account_registration.state_input.fill(state)

        logger.debug(f'Entering city: {city}')
        await self.account_registration.city_input.fill(city)

        logger.debug(f'Entering zipcode: {zipcode}')
        await self.account_registration.zipcode_input.fill(zipcode)

        logger.debug(f'Entering mobile number: {mobile_number}')
        await self.account_registration.mobile_number_input.fill(mobile_number)

        logger.debug('Clicking create account button')
        await self.account_registration.create_account_button.click()
