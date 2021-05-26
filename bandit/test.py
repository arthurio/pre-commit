# flake8: noqa
def test(number: int) -> str:
    access_token = "1234"  # nosec: B105
    password = "7890"  # nosec: B105
    print(password)
    # comment
