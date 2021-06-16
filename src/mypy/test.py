def bad_type(a: int) -> None:
    return a


bad_type("string")
bad_type("string")  # type: ignore[arg-type]
bad_type("string")  # type: ignore

complex_dict = {}
complex_dict["bla"] = [1, 2, 3, 4]
complex_dict[2] = "test"  # type: ignore[assignment]
