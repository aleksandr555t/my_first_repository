print("Hello from first git repository")

print("local changes")


def do_something(number: int, word: str) -> str:

    word = word.capitalize()

    return word * number


print(do_something(3, "go"))


from typing import Literal

user: dict[Literal["name", "second_name", "username"], str] = {}
user["name"] = "Alex"


class User:
    def __init__(self, id, name, age, email) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.email = email


def get_user_info(user):
    return f"{user.name} is {user.age} and his email is {user.email}. User_ID: {user.id}"


user1 = User("1_id", "Max", 42, "max@email.com")
print(get_user_info(user1))


from dataclasses import dataclass


@dataclass
class Car:
    id: str
    name: str
    model: str

def car_info(car):
    return f"Car info:  #: {car.id}, name: {car.name}, model: {car.model}"

car_1 = Car("555", "bmw", "M5")
print(car_info(car_1))
