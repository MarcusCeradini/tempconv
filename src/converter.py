ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(c: float) -> float:
    print((c * 9 / 5) + 32)
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    print((f - 32) * 5 / 9)
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    print(c + 273.15)
    if c < ABSOLUTE_ZERO_C:
        raise ValueError("The value is below absolute 0")
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    print(k - 273.15)
    if k < 0:
        raise ValueError("The value is below absolute 0")
    return k - 273.15


def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return float(value)

    if from_unit == "C":
        celsius = float(value)
    elif from_unit == "F":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "K":
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "K":
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Unknown unit: {to_unit}")


convert(100, "C", "F")
convert(32, "F", "C")
convert(0, "C", "K")
