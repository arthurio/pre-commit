def test(number: int) -> str:
    print("The number is {}".format(number))
    print("The number is {number}".format(number=number))
    print("The number is %s" % number)
    print("The number is %(number)s" % {"number": number})
    print("The number is " + number)
