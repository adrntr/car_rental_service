from starlette import status

from app.api.dependencies.data import get_cars
from app.constants.messages import INVALID_DATE_FORMAT_MSG
from app.tests.utils import override_get_cars, get_future_date, client, app

app.dependency_overrides[get_cars] = override_get_cars


def test_get_available_cars_valid():
    """Test fetching available cars with a valid date format."""
    future_date = get_future_date(2)
    response = client.get(f'/cars/?date={future_date}')
    correct_response = [car.get('plate') for car in override_get_cars() if future_date not in car.get('booking_dates')]
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == correct_response


def test_get_available_cars_invalid_date():
    """Test fetching available cars with an invalid date format."""
    response = client.get("/cars/?date=invalid-date")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == INVALID_DATE_FORMAT_MSG
