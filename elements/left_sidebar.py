from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class LeftSidebarElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._sidebar = page.locator('.left-sidebar')

    # --- Category section ---

    @property
    def category_section(self) -> Locator:
        return self._sidebar.get_by_role('heading', name='Category')

    @property
    def women_category(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Women', exact=True)

    @property
    def women_dress_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Dress').first

    @property
    def women_tops_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Tops', exact=True)

    @property
    def women_saree_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Saree', exact=True)

    @property
    def men_category(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Men', exact=True)

    @property
    def men_tshirts_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Tshirts', exact=True)

    @property
    def men_jeans_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Jeans', exact=True)

    @property
    def kids_category(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Kids', exact=True)

    @property
    def kids_dress_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Dress').last

    @property
    def kids_tops_and_shirts_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Tops & Shirts', exact=True)

    # --- Brands section ---

    @property
    def brands_section(self) -> Locator:
        return self._sidebar.get_by_role('heading', name='Brands')

    @property
    def polo_brand_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Polo', exact=True)

    @property
    def hm_brand_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='H&M', exact=True)

    @property
    def madame_brand_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Madame', exact=True)

    @property
    def mast_and_harbour_brand_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Mast & Harbour', exact=True)

    @property
    def babyhug_brand_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Babyhug', exact=True)

    @property
    def allen_solly_junior_brand_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Allen Solly Junior', exact=True)

    @property
    def kookie_kids_brand_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Kookie Kids', exact=True)

    @property
    def biba_brand_link(self) -> Locator:
        return self._sidebar.get_by_role('link', name='Biba', exact=True)
