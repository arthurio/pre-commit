import os
import sys

from utils import set_env


def test(number: int) -> str:
    print(password)
    access_token = "1234"
    password = "7890"

    print(
        "This is a very long text, a bit longer than what is allowed by black and should be reformatted don't you think?"
    )

    if number > 10:
        return None

    return number + 4


test("arthur")
test(os.getenv("NUMBER"))

set_env()

test(int(os.getenv("NUMBER")))
