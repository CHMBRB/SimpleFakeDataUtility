from datetime import date, datetime


class Person:
    """Base Person Class"""
    id: int
    fname: str
    lname: str
    job: str
    payrate: float
    ssn: str
    dob: date

class ContactDetail:
    """Base ContactDetail Class"""
    id: int
    phone: str
    email: str
    address: str
    city: str
    state: str
    zipcode: str

class LaborDetail:
    """Base LaborDetail Class"""
    id: int
    person_id: int
    current_date: date
    time_in: str
    time_out: str