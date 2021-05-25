from utils import set_env
import os
import sys


def test(number: int) -> str:
    print(password)
    access_token = "1234"  # nosec
    password = "7890"  # nosec

    print(password)

    print("This is a very long text, a bit longer than what is allowed by black and should be reformatted don't you think?")

    if number > 10:
        return None

    return number + 4


test("arthur")
test(os.getenv("NUMBER"))

set_env()

test(int(os.getenv("NUMBER")))
class Test:
    pass


class OtherTest:
    def some_method(self):
        ...
    def some_other_method(self):
        ...
