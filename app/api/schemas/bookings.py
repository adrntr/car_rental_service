from fastapi import HTTPException
from pydantic import BaseModel, field_validator
from starlette import status

from app.constants.messages import INVALID_DATE_FORMAT_MSG, DATE_IN_PAST_MSG, EXCEEDS_BOOKING_WINDOW_MSG
from app.utils.date_validation import is_valid_date, is_future_date, is_within_booking_window
from app.constants.settings import MAX_BOOKING_DAYS

class BookingRequest(BaseModel):
    date: str
    car_plate: str

    @field_validator("date")
    @classmethod
    def validate_date(cls, date_str: str) -> str:
        """
        Validates the given date string based on the following criteria:

        - Must be in the "DD/MM/YYYY" format and represent a valid date.
        - Must be a future date
        - Must not be too far in the future.
        """

        if not is_valid_date(date_str):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=INVALID_DATE_FORMAT_MSG)
        if not is_future_date(date_str):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=DATE_IN_PAST_MSG)
        if not is_within_booking_window(date_str, MAX_BOOKING_DAYS):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=EXCEEDS_BOOKING_WINDOW_MSG)

        return date_str
