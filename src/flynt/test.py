import logging


def test(number: int) -> str:
    print(f"The number is {number}")
    print(f"The number is {number}")
    print(f"The number is {number}")
    print(f"The number is {number}")
    print("The number is " + number)

    logging.info("This is a %s", "test")
