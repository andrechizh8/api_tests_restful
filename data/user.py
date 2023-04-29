import random
from faker import Faker
from dataclasses import dataclass
from typing import Literal


@dataclass
class User:
    first_name: str
    last_name: str
    update_first_name: str
    update_last_name: str
    total_price: int
    checkin: str
    checkout: str
    additional_needs: str
    deposit_paid: Literal["false", "true"]


faker = Faker()

deposit = ["false", "true"]
user = User(first_name=faker.first_name(), last_name=faker.last_name(), update_first_name=faker.first_name(),
            update_last_name=faker.last_name(),
            total_price=random.randrange(100, 1000), checkin='2019-12-10', checkout='2019-01-01',
            additional_needs=faker.job(),
            deposit_paid=random.choice(deposit))

