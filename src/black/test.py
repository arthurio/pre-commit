# flake8:noqa
from typing import Dict



def test_a_giant_named_function_with_a_lot_of_parameters(number: int, a_gigantic_amount_of_parameters: Dict[str, str], it_will_be_too_long: str = "It certainly will") -> str:

    access_token = "1234"  # nosec



    password = "7890"  # nosec
    this_is_weird = {
        # Test a comment
        "test": {"something": "is", "wrong": True}
    }

    print(
        "This is a very long text, a bit longer than what is allowed by black and should be reformatted don't you think?"
    )

    another_bad_thing = True
