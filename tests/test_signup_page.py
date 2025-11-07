import pytest
from playwright.sync_api import expect, Locator

from tests.preconditions import SignupPageNotRegisteredUser


class TestSignupPageNotRegistered(SignupPageNotRegisteredUser):

    def test_register_new_user(self):
        """
        Test verifies that new user can be registered via signup page.

        Note:
        Due to reCAPTCHA presence on the signup page, test ends on verification of recaptcha presence.
        """
        self.signup_page.register_user(email_or_mobile=self.faker.free_email(),
                                       password=self.faker.password(),
                                       full_name=self.faker.name(),
                                       username=f'{self.faker.user_name()}{self.faker.random_int(1000, 9999)}',
                                       month=self.faker.month_name(),
                                       day=self.faker.day_of_month(),
                                       year=self.faker.random_int(min=1970, max=2005))
        expect(self.signup_page.recaptcha_iframe,
               message="Required element not displayed. User registration wasn't completed").to_be_visible()

    @pytest.mark.parametrize('input_field, error_message', [('email_or_phone_input', 'incorrect_email_error_message'),
                                                            ('password_input', 'incorrect_password_error_message'),
                                                            ('username_input', 'username_taken_error_message')])
    def test_incorrect_value_input(self, input_field, error_message):
        """
        Test verifies that appropriate error message is displayed when incorrect value is
        entered in mandatory input fields

        :param input_field: locator of the tested input field
        :param error_message: locator of the dedicated error message
        """
        input_field: Locator = getattr(self.signup_page, input_field)
        error_message: Locator = getattr(self.signup_page, error_message)

        input_field.fill('aaaa')
        self.signup_page.full_name_input.click()

        expect(error_message, message=f"Expected {error_message.text_content()=} for incorrect input "
                                      f"in {input_field.text_content()} not displayed").to_be_visible()
