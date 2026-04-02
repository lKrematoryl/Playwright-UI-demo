from loguru import logger
from playwright.async_api import Page

from pages.base_page import BasePage
from utils.element_builder import ElementBuilder
from utils.models import RegistrationData


class AccountInformationPage(BasePage):

    def __init__(self, page: Page, element_builder: ElementBuilder):
        super().__init__(page)
        self.header = element_builder.header
        self.footer = element_builder.footer
        self.account_registration = element_builder.create_account_registration()

    @property
    def url(self) -> str:
        return f'{super(BasePage).url}/signup'

    async def register_user(self, data: RegistrationData) -> RegistrationData:
        logger.info('Registering new user')

        logger.debug(f'Selecting title: {data.title}')
        if data.title == 'Mr':
            await self.account_registration.title_mr.check()
        else:
            await self.account_registration.title_mrs.check()

        logger.debug(f'Entering password: {data.password}')
        await self.account_registration.password_input.fill(data.password)

        logger.debug(f'Selecting day: {data.day}, month: {data.month}, year: {data.year}')
        await self.account_registration.day_select.select_option(data.day)
        await self.account_registration.month_select.select_option(data.month)
        await self.account_registration.year_select.select_option(data.year)

        logger.debug(f'Entering first name: {data.first_name}')
        await self.account_registration.first_name_input.fill(data.first_name)

        logger.debug(f'Entering last name: {data.last_name}')
        await self.account_registration.last_name_input.fill(data.last_name)

        logger.debug(f'Entering company: {data.company}')
        await self.account_registration.company_input.fill(data.company)

        logger.debug(f'Entering address1: {data.address1}')
        await self.account_registration.address1_input.fill(data.address1)

        logger.debug(f'Entering address2: {data.address2}')
        await self.account_registration.address2_input.fill(data.address2)

        logger.debug(f'Selecting country: {data.country}')
        await self.account_registration.country_select.select_option(data.country)

        logger.debug(f'Entering state: {data.state}')
        await self.account_registration.state_input.fill(data.state)

        logger.debug(f'Entering city: {data.city}')
        await self.account_registration.city_input.fill(data.city)

        logger.debug(f'Entering zipcode: {data.zipcode}')
        await self.account_registration.zipcode_input.fill(data.zipcode)

        logger.debug(f'Entering mobile number: {data.mobile_number}')
        await self.account_registration.mobile_number_input.fill(data.mobile_number)

        logger.debug('Clicking create account button')
        await self.account_registration.create_account_button.click()

        return data
