from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class CartFilledElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('#cart_items')

    @property
    def proceed_to_checkout_button(self) -> Locator:
        return self._section.get_by_role('link', name='Proceed To Checkout')

    @property
    def cart_rows(self) -> Locator:
        return self._section.locator('#cart_info_table tbody tr')

    @property
    def item_image(self) -> Locator:
        return self.cart_rows.locator('td.cart_product img')

    @property
    def item_name(self) -> Locator:
        return self.cart_rows.locator('td.cart_description h4 a')

    @property
    def item_category(self) -> Locator:
        return self.cart_rows.locator('td.cart_description p')

    @property
    def item_price(self) -> Locator:
        return self.cart_rows.locator('td.cart_price p')

    @property
    def item_quantity(self) -> Locator:
        return self.cart_rows.locator('td.cart_quantity button')

    @property
    def item_total(self) -> Locator:
        return self.cart_rows.locator('td.cart_total p.cart_total_price')

    @property
    def item_delete_button(self) -> Locator:
        return self.cart_rows.locator('td.cart_delete a.cart_quantity_delete')
