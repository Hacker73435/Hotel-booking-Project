from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import get_connection
from datetime import date
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title="Hotel Booking System")

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"success": False, "error": None}  # ✅ Always pass context
    )


@app.post("/book", response_class=HTMLResponse)
async def book_room(
    request: Request,
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    check_in: date = Form(...),
    check_out: date = Form(...),
    room_type: str = Form(...),
    num_guests: int = Form(...),
    special_requests: str = Form(""),
):
    success = False
    error = None
    try:
        conn = get_connection()
        conn.run(
            "INSERT INTO bookings (full_name, email, phone, check_in, check_out, room_type, num_guests, special_requests) "
            "VALUES (:full_name, :email, :phone, :check_in, :check_out, :room_type, :num_guests, :special_requests)",
            full_name=full_name,
            email=email,
            phone=phone,
            check_in=str(check_in),
            check_out=str(check_out),
            room_type=room_type,
            num_guests=num_guests,
            special_requests=special_requests,
        )
        conn.close()
        success = True
    except Exception as e:
        print("DB Error:", e)
        error = "Something went wrong while saving your booking. Please try again."  # ✅ Show error to user

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"success": success, "name": full_name, "error": error}
    )
