# flake8: noqa
import random


def test(number: int) -> str:
    access_token = "1234"
    password = "7890"  # nosec: B105
    print(password)

    print(random.randint(0, 1000))
    # comment

    assert False is False
