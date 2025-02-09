# FastAPI Car Rental Service

## **Design Choices**

### **1. Routers: Separation of Concerns**
- The project structure follows the **Single Responsibility Principle (SRP)**.
- **`app/routes/cars.py`** handles car-related endpoints.
- **`app/routes/bookings.py`** manages booking-related endpoints.
- This separation allows future expansion, e.g., adding `GET /car/{id}`, `DELETE /car/{id}`, etc.
---
### **2. Dependency Injection for Data Handling**
- It allows easy swapping of data sources (e.g., in-memory list → database in the future).
- `cars_dependency` is used in endpoints to inject data dynamically.
- This makes testing easier by overriding the data source when needed.
---

### **3. Pydantic for Booking Request Validation**
- **Pydantic** is used to validate and enforce the expected structure of request data.
- Ensures that **dates are correctly formatted** before processing.
---
### **4. Test Data is Dynamically Generated**
- Tests create new data based on the execution date.
- The `get_cars` function is overridden during testing.
---

## **Running the Project**

### **1. Running the Tests**
To execute test cases:
```bash
pip install -r requirements.txt
pytest
```

### **2. Running the FastAPI App**
Start the application using Docker Compose:
```bash
docker compose up -d
```
Once running, open **Swagger UI** at:
```
http://127.0.0.1:8000/docs
```
This allows easy interaction with the API endpoints.
