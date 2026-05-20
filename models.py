from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class BookingModel(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    check_in: date
    check_out: date
    room_type: str
    num_guests: int
    special_requests: Optional[str] = ""

    class Config:
        json_schema_extra = {
            "example": {
                "full_name": "Ali Ahmed",
                "email": "ali@example.com",
                "phone": "0300-1234567",
                "check_in": "2025-06-01",
                "check_out": "2025-06-05",
                "room_type": "Deluxe",
                "num_guests": 2,
                "special_requests": "Late check-in please",
            }
        }
