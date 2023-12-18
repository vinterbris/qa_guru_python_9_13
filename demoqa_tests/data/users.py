from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subjects: list
    hobbies: list
    picture: str
    current_address: str
    state: str
    city: str


student = User(
    first_name='Sergey',
    last_name='Dobrovolskiy',
    email='dobrovolskiy@qa.ru',
    gender='Male',
    phone_number='1002003040',
    day_of_birth='02', month_of_birth='January', year_of_birth='2100',
    subjects=['Maths', 'Chemistry'],
    hobbies=['Sports', 'Reading', 'Music'],
    picture='nolan.jpg',
    current_address='Test Address',
    state='NCR', city='Delhi'
)
