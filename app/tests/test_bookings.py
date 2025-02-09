from starlette import status
from app.api.dependencies.data import get_cars
from app.constants.messages import CAR_ALREADY_BOOKED_MSG
from app.tests.utils import override_get_cars, get_future_date, client, sample_car, app

app.dependency_overrides[get_cars] = override_get_cars


def test_book_car_success(sample_car):
    """Test successfully booking a car."""
    future_date = get_future_date(30)
    response = client.put("/bookings/book/", json={"date": future_date, "car_plate": sample_car.get('plate')})
    assert response.status_code == status.HTTP_204_NO_CONTENT

    car = next(car for car in override_get_cars() if car["plate"] == sample_car['plate'])
    assert future_date in car["booking_dates"]


def test_book_car_already_booked(sample_car):
    """Test booking a car that is already booked on the same date."""
    future_date = get_future_date(50)
    client.put("/bookings/book/", json={"date": future_date, "car_plate": sample_car['plate']})

    response = client.put("/bookings/book/", json={"date": future_date, "car_plate": sample_car['plate']})
    assert response.status_code == 400
    assert response.json()["detail"] == CAR_ALREADY_BOOKED_MSG
