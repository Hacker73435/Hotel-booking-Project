from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import get_connection
from datetime import date
import uvicorn

app = FastAPI(title="Hotel Booking System")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO bookings (full_name, email, phone, check_in, check_out, room_type, num_guests, special_requests)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (full_name, email, phone, check_in, check_out, room_type, num_guests, special_requests),
    )
    conn.commit()
    cursor.close()
    conn.close()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "success": True,
            "name": full_name,
        },
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
