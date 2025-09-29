from datetime import date


def validate_pesel_format(pesel: str) -> bool:
    """
    Validate basic PESEL format.

    Args:
        pesel: PESEL number to validate.

    Returns:
        True if format is valid (11 digits), False otherwise.
    """

    if not isinstance(pesel, str):
        return False
    elif len(pesel) != 11:
        return False
    elif not pesel.isdigit():
        return False

    return True

def calculate_checksum(pesel: str) -> int:
    """
    Calculate PESEL checksum digit.

    Args:
        pesel: PESEL number (assumes valid format).

    Returns:
        Expected checksum digit (0-9).
    """

    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    total = 0

    for i, weight in enumerate(weights):
        total += int(pesel[i]) * weight

    remainder = total % 10
    return (10 - remainder) % 10

def extract_gender(pesel: str) -> str:
    """
    Extract gender from PESEL number.

    Args:
        pesel: PESEL number (assumes valid format).

    Returns:
        "Female" for even digit, "Male" for odd digit.
    """

    gender_digit = int(pesel[9])
    if gender_digit % 2 == 0:
        return "Female"
    else:
        return "Male"


def extract_birth_date(pesel: str) -> date | None:
    """
    Extract birth date from PESEL number.

    Args:
        pesel: PESEL number (assumes valid format).

    Returns:
        Date object with birth date, or None if date is invalid.
    """

    year_digits = int(pesel[0:2])
    month_coded = int(pesel[2:4])
    day = int(pesel[4:6])

    if 1 <= month_coded <= 12:
        century = 1900
        month = month_coded
    elif 21 <= month_coded <= 32:
        century = 2000
        month = month_coded - 20
    elif 81 <= month_coded <= 92:
        century = 1800
        month = month_coded - 80
    elif 41 <= month_coded <= 52:
        century = 2100
        month = month_coded - 40
    elif 61 <= month_coded <= 72:
        century = 2200
        month = month_coded - 60
    else:
        return None

    full_year = century + year_digits

    try:
        return date(full_year, month, day)
    except ValueError:
        return None

def validate_pesel(pesel: str) -> dict:
    """
    Validate PESEL number and extract information.

    Args:
        pesel: PESEL number to validate.

    Returns:
        Dictionary with validation results:
        - valid: bool
        - birth_date: date or None
        - gender: str or None
        - error: str or None
    """

    if not validate_pesel_format(pesel):
        return {
            "valid": False,
            "birth_date": None,
            "gender": None,
            "error": "Invalid PESEL format"
        }

    birth_date = extract_birth_date(pesel)
    if birth_date is None:
        return {
            "valid": False,
            "birth_date": None,
            "gender": None,
            "error": "Invalid birth date"
        }

    expected_checksum = calculate_checksum(pesel)
    actual_checksum = int(pesel[10])

    if expected_checksum != actual_checksum:
        return {
            "valid": False,
            "birth_date": None,
            "gender": None,
            "error": "Invalid checksum"
        }

    return {
        "valid": True,
        "birth_date": birth_date,
        "gender": extract_gender(pesel),
        "error": None
    }
