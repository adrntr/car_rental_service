from datetime import datetime, timedelta


def is_valid_date(date_str: str) -> bool:
    """Check if the date is in valid DD/MM/YYYY format and is a real date."""
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def is_future_date(date_str: str) -> bool:
    """Check if the date is in the future."""
    input_date = datetime.strptime(date_str, "%d/%m/%Y")
    return input_date >= datetime.now()


def is_within_booking_window(date_str: str, max_booking_days: int) -> bool:
    """Check if the date is within the allowed booking period (e.g., max 1 year)."""
    input_date = datetime.strptime(date_str, "%d/%m/%Y")
    max_date = datetime.now() + timedelta(days=max_booking_days)
    return input_date <= max_date
