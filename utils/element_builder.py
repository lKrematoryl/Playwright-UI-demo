from functools import cached_property

from playwright.async_api import Page

from elements.shared.header import HeaderElement
from elements.shared.footer import FooterElement
from elements.shared.left_sidebar import LeftSidebarElement
from elements.shared.breadcrumb import BreadcrumbElement
from elements.home.slider import SliderElement
from elements.products.advertisement import AdvertisementElement
from elements.products.product_card import ProductCardElement
from elements.home.features_items import FeaturesItemsElement
from elements.home.recommended_items import RecommendedItemsElement
from elements.auth.login_form import LoginFormElement
from elements.auth.signup_form import SignupFormElement
from elements.contact.contact_us import ContactUsElement
from elements.auth.account_registration import AccountRegistrationElement
from elements.auth.account_created import AccountCreatedElement
from elements.cart.cart_empty import CartEmptyElement
from elements.cart.cart_filled import CartFilledElement
from elements.modals.checkout_modal import CheckoutModalElement
from elements.checkout.address_details import AddressDetailsElement
from elements.checkout.order_review import OrderReviewElement
from elements.checkout.order_comment import OrderCommentElement
from elements.payment.payment_form import PaymentFormElement
from elements.payment.order_placed import OrderPlacedElement


class ElementBuilder:
    """
    Dedicated builder for page element objects.
    - @cached_property for elements shared across pages (header, footer, sidebar, breadcrumb) —
      guarantees a single instance per test.
    - create_* methods for page-specific elements that are unique per page.
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

    @cached_property
    def breadcrumb(self) -> BreadcrumbElement:
        return BreadcrumbElement(self.page)

    # --- Page-specific elements ---

    def create_slider(self) -> SliderElement:
        return SliderElement(self.page)

    def create_advertisement(self) -> AdvertisementElement:
        return AdvertisementElement(self.page)

    def create_product_card(self) -> ProductCardElement:
        return ProductCardElement(self.page)

    def create_features_items(self) -> FeaturesItemsElement:
        return FeaturesItemsElement(self.page)

    def create_recommended_items(self) -> RecommendedItemsElement:
        return RecommendedItemsElement(self.page)

    def create_login_form(self) -> LoginFormElement:
        return LoginFormElement(self.page)

    def create_signup_form(self) -> SignupFormElement:
        return SignupFormElement(self.page)

    def create_contact_us(self) -> ContactUsElement:
        return ContactUsElement(self.page)

    def create_account_registration(self) -> AccountRegistrationElement:
        return AccountRegistrationElement(self.page)

    def create_account_created(self) -> AccountCreatedElement:
        return AccountCreatedElement(self.page)

    def create_cart_empty(self) -> CartEmptyElement:
        return CartEmptyElement(self.page)

    def create_cart_filled(self) -> CartFilledElement:
        return CartFilledElement(self.page)

    def create_checkout_modal(self) -> CheckoutModalElement:
        return CheckoutModalElement(self.page)

    def create_address_details(self) -> AddressDetailsElement:
        return AddressDetailsElement(self.page)

    def create_order_review(self) -> OrderReviewElement:
        return OrderReviewElement(self.page)

    def create_order_comment(self) -> OrderCommentElement:
        return OrderCommentElement(self.page)

    def create_payment_form(self) -> PaymentFormElement:
        return PaymentFormElement(self.page)

    def create_order_placed(self) -> OrderPlacedElement:
        return OrderPlacedElement(self.page)
