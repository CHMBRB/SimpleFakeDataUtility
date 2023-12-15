from faker import Faker
from .DataClasses import Person, ContactDetail, LaborDetail

# seed to make our data reproducable
Faker.seed(0)

# add localization
f = Faker('en-US')

class FakePerson(Person):
    """FakePerson Derived Person Class"""
    def __init__(self, id:int):
        self.id = id
        self.fname = f.first_name()
        self.lname = f.last_name()
        self.job = f.job()
        self.payrate = f.pyfloat(right_digits=2, positive=True, min_value=15.00, max_value=45.00)
        self.ssn = f.ssn()
        self.dob = f.date_between(start_date='-80y',end_date='-18y')


class FakeContactDetail(ContactDetail):
    """FakeContactDetail Derived ContactDetail Class"""
    def __init__(self, id):
        self.id = id
        self.phone = f.phone_number()
        self.email = f.email(domain='example.com')
        self.address = f.street_address()
        self.city = f.city()
        self.state = f.state()
        self.zipcode = f.postcode()