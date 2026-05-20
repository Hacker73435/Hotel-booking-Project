# Hotel Booking System – FastAPI + PostgreSQL

A full-stack hotel booking form built with HTML, FastAPI, and PostgreSQL, deployed live on Vercel.

---

## Project Structure

```
hotel-booking-project/
├── api/
│   └── index.py          ← Vercel entry point (imports main app)
├── main.py               ← FastAPI routes
├── database.py           ← PostgreSQL connection
├── models.py             ← Pydantic data model
├── templates/
│   └── index.html        ← Booking form (Jinja2)
├── static/
│   └── style.css         ← Styling
├── sql/
│   └── create_table.sql  ← Run once to create DB table
├── .env                  ← Your credentials (never commit this)
├── .gitignore
├── requirements.txt
├── vercel.json           ← Vercel config
└── README.md
```

---

## STEP 1 — Get a Free Online Database (Neon)

1. Go to **https://neon.tech** and sign up for free
2. Click **"New Project"** → give it any name (e.g. `hotel-db`)
3. Once created, click **"Connection string"**
4. Copy the string — it looks like:
   ```
   postgresql://alex:password@ep-cool-123.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```
5. Keep this URL — you'll need it in Steps 2 and 4

---

## STEP 2 — Create the Database Table

1. On the Neon dashboard, click **"SQL Editor"**
2. Paste and run this SQL:

```sql
CREATE TABLE IF NOT EXISTS bookings (
    id               SERIAL PRIMARY KEY,
    full_name        VARCHAR(150)  NOT NULL,
    email            VARCHAR(150)  NOT NULL,
    phone            VARCHAR(30)   NOT NULL,
    check_in         DATE          NOT NULL,
    check_out        DATE          NOT NULL,
    room_type        VARCHAR(50)   NOT NULL,
    num_guests       INTEGER       NOT NULL CHECK (num_guests >= 1),
    special_requests TEXT          DEFAULT '',
    created_at       TIMESTAMP     DEFAULT CURRENT_TIMESTAMP
);
```

3. Click **Run** — you should see "Success"

---

## STEP 3 — Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit - hotel booking project"
```

Create a new repo on GitHub (github.com → New repository), then:

```bash
git remote add origin https://github.com/YOUR_USERNAME/hotel-booking-project.git
git branch -M main
git push -u origin main
```

> Make sure `.env` is in `.gitignore` — your database password must NOT go to GitHub.

---

## STEP 4 — Deploy on Vercel

1. Go to **https://vercel.com** and sign in with GitHub
2. Click **"Add New Project"**
3. Import your `hotel-booking-project` repository
4. Before clicking Deploy, go to **"Environment Variables"** and add:

   | Key | Value |
   |-----|-------|
   | `DATABASE_URL` | (paste your Neon connection string from Step 1) |

5. Click **Deploy**
6. Wait ~1 minute — Vercel will give you a live URL like:
   ```
   https://hotel-booking-project-xyz.vercel.app
   ```

---

## STEP 5 — Test & Submit

1. Open your live Vercel URL
2. Fill in the booking form and submit
3. Check Neon SQL Editor — run `SELECT * FROM bookings;` to confirm data was saved
4. Copy the live URL and paste it into a document
5. Upload that document to the LMS

---

## Running Locally (Optional)

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

Edit `.env` and paste your Neon DATABASE_URL, then:

```bash
uvicorn main:app --reload
```

Open: http://127.0.0.1:8000
