import logging


def test(number: int) -> str:
    print("The number is {}".format(number))
    print("The number is %d" % number)
    print("The number is {number}".format(number=number))
    print(f"The number is {number}")
    print("The number is " + number)

    logging.info("This is a %s", "test")
