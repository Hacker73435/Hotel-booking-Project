 Hotel Booking System

A full-stack hotel booking web application built with FastAPI, PostgreSQL, and Jinja2 templates — deployed on Vercel.

Show Image
Show Image
Show Image
Show Image

🌐 Live Demo
👉 hotel-booking-project-one.vercel.app

📌 Features

🏨 Simple and clean hotel booking form
⚡ FastAPI backend — high performance Python API
🗄️ PostgreSQL database integration
🎨 Clean UI with HTML/CSS via Jinja2 templates
☁️ Deployed and ready on Vercel
🔐 Environment variables support via .env


📁 Project Structure
hotel-booking-project/
│
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
├── .env                  # Environment variables (not committed)
├── .gitignore
├── requirements.txt
├── vercel.json
└── README.md

⚙️ Local Setup
1. Clone the repository
bashgit clone https://github.com/your-username/hotel-booking-project.git
cd hotel-booking-project
2. Create virtual environment
bashpython -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
3. Install dependencies
bashpip install -r requirements.txt
4. Setup environment variables
Create a .env file in the root folder:
DATABASE_URL=your_postgresql_connection_string
5. Setup database
Run the SQL script in your PostgreSQL client:
bashpsql -U your_user -d your_database -f sql/create_table.sql
6. Run locally
bashuvicorn main:app --reload
Then open: http://127.0.0.1:8000

☁️ Deployment on Vercel

Push your project to GitHub
Go to vercel.com → Import project
Add environment variable in Vercel dashboard:

   DATABASE_URL = your_postgresql_connection_string

Click Deploy 🚀


🛠️ Tech Stack
LayerTechnologyBackendFastAPI (Python)DatabasePostgreSQLTemplatesJinja2FrontendHTML5, CSS3DeploymentVercel

👨‍💻 Developer
Arslan Saeed

🎓 University of Management and Technology (UMT), Lahore
🏛️ Department of Cyber Security
📧 arslanbrall@gmail.com


📄 License
This project is open source and available under the MIT License.
