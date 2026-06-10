🏨 Hotel Booking System – FastAPI + PostgreSQL

A full-stack hotel booking web application built using FastAPI, PostgreSQL, HTML/CSS (Jinja2 templates) and deployed on Vercel.

🚀 Live Project

(https://hotel-booking-project-one.vercel.app/)
📌 Features

🏨 Simple hotel booking form
⚡ FastAPI backend (high performance API)
🗄️ PostgreSQL database integration
🎨 Clean UI using HTML + CSS (Jinja2 templates)
☁️ Ready for deployment on Vercel
🔐 Environment variables support (.env)
📁 Project Structure


hotel-booking-project/
├── api/
│   └── index.py          # Vercel entry point
├── main.py               # FastAPI routes
├── database.py           # PostgreSQL connection
├── models.py             # Pydantic models
├── templates/
│   └── index.html        # Booking form UI
├── static/
│   └── style.css         # Styling
├── sql/
│   └── create_table.sql  # Database table schema
├── .env                  # Environment variables
├── .gitignore
├── requirements.txt
├── vercel.json
└── README.md

⚙️ Installation & Setup

1. Clone the repository
   
git clone https://github.com/your-username/hotel-booking-project.git
cd hotel-booking-project
3. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
4. Install dependencies
pip install -r requirements.txt
5. Setup environment variables

Create a .env file:

DATABASE_URL=your_postgresql_connection_string
5. Run database script

Run this in PostgreSQL:

sql/create_table.sql
6. Run the project locally
uvicorn main:app --reload

Then open:

http://127.0.0.1:8000
☁️ Deployment (Vercel)
Push project to GitHub
Connect repository to Vercel
Set environment variables in Vercel dashboard
Deploy 🚀
🛠️ Tech Stack
FastAPI
PostgreSQL
Jinja2 Templates
HTML/CSS
Vercel
Python

                       📸 UI Preview

(<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3d530bd2-d9e4-4bf0-8636-694959d99720" />
)
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/614621b9-75af-4f02-801e-9e65f5f2c3c8" />

👨‍💻 Author
 Name: Arslan Saeed
University: UMT
Field: Cyber Security Student
📄 License

This project is for academic/learning purposes.
