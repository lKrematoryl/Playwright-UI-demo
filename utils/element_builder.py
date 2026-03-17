from functools import cached_property

from playwright.async_api import Page

from elements.header import HeaderElement
from elements.footer import FooterElement
from elements.sidebar import LeftSidebarElement
from elements.slider import SliderElement
from elements.advertisement import AdvertisementElement
from elements.product_card import ProductCardElement
from elements.login_form import LoginSectionElement
from elements.signup_form import SignupSectionElement
from elements.contact_us import ContactUsElement


class ElementBuilder:
    """
    Dedicated builder for page element objects.
    - @cached_property for elements shared across pages (header, footer, sidebar) —
      guarantees a single instance per test.
    - create_* methods for elements that are page-specific or may need a fresh instance.
    Extend this builder when a new page element is added to the framework.
    """

    def __init__(self, page: Page):
        self.page = page

    # --- Shared elements (cached, one instance per test) ---

    @cached_property
    def header(self) -> HeaderElement:
        return HeaderElement(self.page)

    @cached_property
    def footer(self) -> FooterElement:
        return FooterElement(self.page)

    @cached_property
    def left_sidebar(self) -> LeftSidebarElement:
        return LeftSidebarElement(self.page)

    # --- Page-specific elements (fresh instance per page) ---

    def create_slider(self) -> SliderElement:
        return SliderElement(self.page)

    def create_advertisement(self) -> AdvertisementElement:
        return AdvertisementElement(self.page)

    def create_product_card(self) -> ProductCardElement:
        return ProductCardElement(self.page)

    def create_login_form(self) -> LoginSectionElement:
        return LoginSectionElement(self.page)

    def create_signup_form(self) -> SignupSectionElement:
        return SignupSectionElement(self.page)

    def create_contact_us(self) -> ContactUsElement:
        return ContactUsElement(self.page)

