from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class OrderReviewElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._section = page.locator('#cart_info')

    @property
    def heading(self) -> Locator:
        return self.page.locator('div.step-one').get_by_role('heading', name='Review Your Order')

    @property
    def cart_rows(self) -> Locator:
        return self._section.locator('tbody tr:not(:last-child)')

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
    def total_amount(self) -> Locator:
        return self._section.locator('tbody tr:last-child p.cart_total_price')
