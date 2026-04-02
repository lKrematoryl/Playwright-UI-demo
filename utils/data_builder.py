from faker import Faker

from utils.models import RegistrationData


class DataBuilder:
    """
    Dedicated builder for test data objects.
    Follows the same pattern as PageBuilder and ElementBuilder.
    Extend this builder when new test data models are added to the framework.
    """

    def __init__(self, faker: Faker):
        self._faker = faker
        self.registration_template = RegistrationData

    @property
    def valid_user(self) -> RegistrationData:
        return self.registration_template.valid(self._faker)

    @property
    def invalid_user(self) -> RegistrationData:
        return self.registration_template.invalid(self._faker)

    def custom_user(self, **overrides) -> RegistrationData:
        return self.registration_template.valid(self._faker, **overrides)

    @property
    def empty_fields(self):
        return self.registration_template.empty_fields()
