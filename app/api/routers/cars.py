from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from typing_extensions import Annotated

from app.api.dependencies.data import get_cars
from app.constants.messages import INVALID_DATE_FORMAT_MSG
from app.utils.date_validation import is_valid_date

router = APIRouter(
    prefix='/cars',
    tags=['cars']
)

cars_dependency = Annotated[dict, Depends(get_cars)]


@router.get('/', status_code=status.HTTP_200_OK)
async def get_available_cars(cars: cars_dependency, date: str) -> list:
    """
    Retrieves a list of available cars for a given date.

    This endpoint filters out cars that have existing bookings on the specified date
    and returns the license plates of the available cars.

    Args:
        cars (list): A dependency-injected list of car dictionaries.
        date (str): The requested date in "DD/MM/YYYY" format.

    Returns:
        list: A list of license plates of available cars.

    Raises:
        HTTPException: If the provided date is invalid, returns a 400 Bad Request.
    """
    if not is_valid_date(date):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_DATE_FORMAT_MSG)
    return [car.get("plate") for car in cars if date not in car.get('booking_dates', [])]
