# 🩺 Prescripto — Doctor Appointment System

A full-stack web application built with **Python Flask** and **SQLite** that allows patients to register, log in, browse doctors, and book appointments online.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Pages & Routes](#pages--routes)
- [Database Schema](#database-schema)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)

---

## ✨ Features

- 🏠 **Landing Page** — Hero section with stats, feature highlights, and doctor previews
- 👤 **Patient Registration** — Full signup form with live password strength meter, confirm password match, and client-side validation
- 🔐 **Patient Login** — Role-based login toggle (Patient / Doctor / Admin) with show/hide password
- 🩺 **Doctor Directory** — Search by name, filter by specialty, availability badges, sort by rating/experience
- 📅 **Appointment Booking** — 3-step booking form with dynamic doctor dropdowns, time slot picker, and booking confirmation with reference number
- 🗄️ **SQLite Database** — Stores patients and appointments persistently
- 📱 **Responsive Design** — Works on desktop, tablet, and mobile
- 🔔 **Toast Notifications** — Live feedback on all user actions
- 🎨 **Modern UI** — Deep Navy + Teal color system, Google Fonts, smooth animations

---

## 🛠 Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3.9+, Flask 3.0            |
| Database   | SQLite3 (built into Python)       |
| Frontend   | HTML5, CSS3, Vanilla JavaScript   |
| Fonts      | Google Fonts (Cormorant Garamond + DM Sans) |
| Templating | Jinja2 (via Flask)                |

---

## 📁 Project Structure

```
Prescripto/
│
├── app.py                  # Main Flask application & all routes
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
├── database/
│   └── database.db         # SQLite database (auto-created on first run)
│
├── static/
│   ├── css/
│   │   └── style.css       # Full design system & all page styles
│   └── js/
│       └── script.js       # Global JS: navbar scroll, toast alerts, animations
│
└── templates/
    ├── index.html           # Home / Landing page
    ├── register.html        # Patient signup
    ├── login.html           # Patient / Doctor / Admin login
    ├── doctors.html         # Doctor listing with search & filter
    └── appointment.html     # 3-step appointment booking form
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.9 or higher** — [Download here](https://www.python.org/downloads/)
- pip (comes bundled with Python)

### 1. Clone or Download the Project

```bash
# If using Git
git clone https://github.com/saptshrungikadole/prescripto.git
cd prescripto

# Or simply open the Prescripto folder in VS Code
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

> The SQLite database and `database/` folder are created **automatically** on first run. No setup needed.

---

## 🗺 Pages & Routes

| Route          | Method     | Description                              |
|----------------|------------|------------------------------------------|
| `/`            | GET        | Home / landing page                      |
| `/register`    | GET, POST  | Patient registration form                |
| `/login`       | GET, POST  | Login for patients, doctors, and admins  |
| `/logout`      | GET        | Clears session and redirects to login    |
| `/doctors`     | GET        | Browse and filter doctor listings        |
| `/appointment` | GET, POST  | 3-step appointment booking form          |

---

## 🗄 Database Schema

### `patients` table

| Column       | Type    | Description                        |
|--------------|---------|------------------------------------|
| id           | INTEGER | Primary key, auto-incremented      |
| first_name   | TEXT    | Patient's first name               |
| last_name    | TEXT    | Patient's last name                |
| email        | TEXT    | Unique email address               |
| phone        | TEXT    | Phone number                       |
| dob          | TEXT    | Date of birth                      |
| gender       | TEXT    | Gender                             |
| password     | TEXT    | Password (plain text — see note)   |
| created_at   | DATETIME| Record creation timestamp          |

### `appointments` table

| Column     | Type    | Description                          |
|------------|---------|--------------------------------------|
| id         | INTEGER | Primary key, auto-incremented        |
| patient    | TEXT    | Patient's full name                  |
| phone      | TEXT    | Patient's phone number               |
| email      | TEXT    | Patient's email                      |
| doctor     | TEXT    | Selected doctor's name               |
| specialty  | TEXT    | Doctor's specialty                   |
| date       | TEXT    | Appointment date                     |
| time_slot  | TEXT    | Selected time slot                   |
| appt_type  | TEXT    | in-person / video / phone            |
| reason     | TEXT    | Reason for visit                     |
| status     | TEXT    | confirmed / cancelled (default: confirmed) |
| created_at | DATETIME| Booking timestamp                    |

---

## 🔮 Future Improvements

These features would make the project production-ready and stronger for your resume/portfolio:

- [ ] **Password Hashing** — Use `werkzeug.security` (`generate_password_hash` / `check_password_hash`) instead of storing plain text passwords
- [ ] **Admin Dashboard** — View all appointments, manage doctors, see analytics
- [ ] **Doctor Login** — Separate portal for doctors to manage their schedule
- [ ] **Appointment History** — Patient dashboard to view, reschedule, or cancel bookings
- [ ] **Email Notifications** — Send confirmation emails using `Flask-Mail` or SendGrid
- [ ] **OTP / Phone Login** — Two-factor authentication via SMS
- [ ] **Doctor Availability Calendar** — Real-time slot management per doctor
- [ ] **Search & Pagination** — Handle large doctor/appointment datasets efficiently
- [ ] **Deploy to Cloud** — Host on Render, Railway, or AWS (replace SQLite with PostgreSQL)

---

## ⚠️ Important Note on Security

> Passwords in this project are stored as **plain text** for simplicity and learning purposes.  
> In a real production app, **always hash passwords** before storing them:

```python
from werkzeug.security import generate_password_hash, check_password_hash

# When registering:
hashed = generate_password_hash(password)

# When logging in:
check_password_hash(hashed, entered_password)
```

---

## 👨‍💻 Author

Built as a learning project to demonstrate Flask, SQLite, and frontend development skills.

Feel free to fork, improve, and use for your own portfolio! ⭐

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
