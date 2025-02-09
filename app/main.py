from fastapi import FastAPI

from app.api.routers import cars, bookings

app = FastAPI()

app.include_router(cars.router)

app.include_router(bookings.router)
