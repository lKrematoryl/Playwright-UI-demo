from playwright.async_api import Page, Locator

from elements.base_element import _BaseElement


class ContactUsElement(_BaseElement):

    def __init__(self, page: Page):
        super().__init__(page)
        self._form = page.locator('.contact-form')
        self._info = page.locator('.contact-info')

    # --- Contact form ---

    @property
    def heading(self) -> Locator:
        return self._form.get_by_role('heading', name='Get In Touch')

    @property
    def name_input(self) -> Locator:
        return self._form.get_by_role('textbox', name='Name')

    @property
    def email_input(self) -> Locator:
        return self._form.get_by_role('textbox', name='Email')

    @property
    def subject_input(self) -> Locator:
        return self._form.get_by_role('textbox', name='Subject')

    @property
    def message_input(self) -> Locator:
        return self._form.get_by_role('textbox', name='Your Message Here')

    @property
    def file_upload(self) -> Locator:
        return self._form.locator('input[name="upload_file"]')

    @property
    def submit_button(self) -> Locator:
        return self._form.get_by_role('button', name='Submit')

    @property
    def success_message(self) -> Locator:
        return self._form.locator('.status.alert.alert-success')

    # --- Contact info ---

    @property
    def info_heading(self) -> Locator:
        return self._info.get_by_role('heading', name='Feedback For Us')

    @property
    def feedback_email_link(self) -> Locator:
        return self._info.get_by_role('link', name='feedback@automationexercise.com')
