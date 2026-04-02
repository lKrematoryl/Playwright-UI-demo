from dataclasses import dataclass
from faker import Faker


@dataclass
class RegistrationData:
    title: str
    name: str
    password: str
    day: str | int
    month: str | int
    year: str | int
    first_name: str
    last_name: str
    company: str
    address1: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str

    @classmethod
    def valid(cls, faker: Faker, **overrides) -> 'RegistrationData':
        defaults = dict(
            title='Mr',
            name=faker.name(),
            password=faker.password(),
            day=str(faker.random_int(min=1, max=28)),
            month=faker.date_object().strftime('%B'),
            year=str(faker.random_int(min=1970, max=2005)),
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            company=faker.company(),
            address1=faker.street_address(),
            address2=faker.secondary_address(),
            country='United States',
            state=faker.state(),
            city=faker.city(),
            zipcode=faker.zipcode(),
            mobile_number=faker.phone_number()
        )
        return cls(**(defaults | overrides))

    @classmethod
    def empty_fields(cls) -> 'RegistrationData':
        return cls(
            title='',
            name='',
            password='',
            day='',
            month='',
            year='',
            first_name='',
            last_name='',
            company='',
            address1='',
            address2='',
            country='',
            state='',
            city='',
            zipcode='',
            mobile_number=''
        )

    @classmethod
    def invalid(cls, faker: Faker) -> 'RegistrationData':
        return cls(
            title='Mr',
            name=faker.name(),
            password='1',
            day='0',
            month='0',
            year='0',
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            company=faker.company(),
            address1=faker.street_address(),
            address2=faker.secondary_address(),
            country='United States',
            state=faker.state(),
            city=faker.city(),
            zipcode='!@#$%',
            mobile_number='not-a-number'
        )
