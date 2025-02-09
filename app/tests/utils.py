from datetime import datetime, timedelta
from fastapi.testclient import TestClient
import pytest
from app.main import app





def get_future_date(days_in_future: int) -> str:
    """
    Calculates the date a given number of days from today and returns it as a string.

    Args:
        days_in_future (int): The number of days to add to today's date.

    Returns:
        str: The future date in "DD/MM/YYYY" format.
    """
    return (datetime.today() + timedelta(days=days_in_future)).strftime("%d/%m/%Y")

OVERRIDE_CARS = [
    {'plate': 'DEF456', 'booking_dates': [get_future_date(1), get_future_date(2)]},
    {'plate': 'GHI789', 'booking_dates': []},
    {'plate': 'MNO987', 'booking_dates': [get_future_date(5), get_future_date(6)]},
    {'plate': 'EFG567', 'booking_dates': [get_future_date(14)]},
    {'plate': 'HIJ890', 'booking_dates': [get_future_date(16), get_future_date(17)]},
    {'plate': 'KLM123', 'booking_dates': []}
]

def override_get_cars():
    """
    Returns a predefined list of cars from the OVERRIDE_CARS variable.

    Returns:
        list: A list of overridden car data.
    """
    return OVERRIDE_CARS

@pytest.fixture
def sample_car():
    """
    Returns a sample car from the predefined list of overridden cars.

    Returns:
        dict or any: The first car in the OVERRIDE_CARS list.
    """
    return OVERRIDE_CARS[0]


client = TestClient(app)
