from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from typing_extensions import Annotated

from app.api.dependencies.data import get_cars
from app.api.schemas.bookings import BookingRequest
from app.constants.messages import CAR_NOT_FOUND_MSG, CAR_ALREADY_BOOKED_MSG

router = APIRouter(
    prefix='/bookings',
    tags=['bookings'],
)

cars_dependency = Annotated[dict, Depends(get_cars)]


@router.put('/book/', status_code=status.HTTP_204_NO_CONTENT)
async def book_car(cars: cars_dependency, request: BookingRequest):
    """
    Books a car for a specified date.

    Args:
        cars (list): A dependency-injected list of car dictionaries.
        request (BookingRequest): The booking request containing the car plate and date.

    Raises:
        HTTPException:
            - 404 Not Found if the car does not exist or data is not valid.
            - 400 Bad Request if the car is already booked for the requested date.

    Returns:
        None: Responds with HTTP 204 No Content on successful booking.
    """

    car = next((car for car in cars if car["plate"] == request.car_plate), None)

    if car is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=CAR_NOT_FOUND_MSG)

    if request.date in car["booking_dates"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=CAR_ALREADY_BOOKED_MSG
        )

    car["booking_dates"].append(request.date)
