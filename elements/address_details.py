from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class AddressDetailsElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('.checkout-information')

    @property
    def heading(self) -> Locator:
        return self._section.locator('..').get_by_role('heading', name='Address Details')

    # --- Delivery address ---

    @property
    def delivery_address(self) -> Locator:
        return self._section.locator('#address_delivery')

    @property
    def delivery_address_heading(self) -> Locator:
        return self.delivery_address.get_by_role('heading', name='Your delivery address')

    @property
    def delivery_full_name(self) -> Locator:
        return self.delivery_address.locator('.address_firstname.address_lastname')

    @property
    def delivery_address1(self) -> Locator:
        return self.delivery_address.locator('.address_address1.address_address2').first

    @property
    def delivery_address2(self) -> Locator:
        return self.delivery_address.locator('.address_address1.address_address2').nth(1)

    @property
    def delivery_city_state_postcode(self) -> Locator:
        return self.delivery_address.locator('.address_city.address_state_name.address_postcode')

    @property
    def delivery_country(self) -> Locator:
        return self.delivery_address.locator('.address_country_name')

    @property
    def delivery_phone(self) -> Locator:
        return self.delivery_address.locator('.address_phone')

    # --- Billing address ---

    @property
    def billing_address(self) -> Locator:
        return self._section.locator('#address_invoice')

    @property
    def billing_address_heading(self) -> Locator:
        return self.billing_address.get_by_role('heading', name='Your billing address')

    @property
    def billing_full_name(self) -> Locator:
        return self.billing_address.locator('.address_firstname.address_lastname')

    @property
    def billing_address1(self) -> Locator:
        return self.billing_address.locator('.address_address1.address_address2').first

    @property
    def billing_address2(self) -> Locator:
        return self.billing_address.locator('.address_address1.address_address2').nth(1)

    @property
    def billing_city_state_postcode(self) -> Locator:
        return self.billing_address.locator('.address_city.address_state_name.address_postcode')

    @property
    def billing_country(self) -> Locator:
        return self.billing_address.locator('.address_country_name')

    @property
    def billing_phone(self) -> Locator:
        return self.billing_address.locator('.address_phone')
