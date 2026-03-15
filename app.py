from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "prescripto_secret_key_2025"

DB_PATH = "database/database.db"

# ── DATABASE SETUP ─────────────────────────────
def init_db():
    if not os.path.exists("database"):
        os.makedirs("database")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name      TEXT NOT NULL,
        last_name       TEXT NOT NULL,
        email           TEXT UNIQUE NOT NULL,
        phone           TEXT,
        dob             TEXT,
        gender          TEXT,
        password        TEXT NOT NULL,
        created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        patient     TEXT NOT NULL,
        phone       TEXT,
        email       TEXT,
        doctor      TEXT NOT NULL,
        specialty   TEXT,
        date        TEXT NOT NULL,
        time_slot   TEXT,
        appt_type   TEXT DEFAULT 'in-person',
        reason      TEXT,
        status      TEXT DEFAULT 'confirmed',
        created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ── ROUTES ────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form.get("first_name", "").strip()
        last_name  = request.form.get("last_name", "").strip()
        email      = request.form.get("email", "").strip()
        phone      = request.form.get("phone", "").strip()
        dob        = request.form.get("dob", "")
        gender     = request.form.get("gender", "")
        password   = request.form.get("password", "")

        # Basic server-side validation
        if not first_name or not last_name or not email or not password:
            flash("Please fill in all required fields.", "error")
            return render_template("register.html")

        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return render_template("register.html")

        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO patients (first_name, last_name, email, phone, dob, gender, password)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (first_name, last_name, email, phone, dob, gender, password)
            )
            conn.commit()
            conn.close()
            flash("Account created successfully! Please log in.", "success")
            return redirect("/login")

        except sqlite3.IntegrityError:
            flash("An account with this email already exists.", "error")
            return render_template("register.html")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, first_name, last_name FROM patients WHERE email=? AND password=?",
            (email, password)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_id"]   = user[0]
            session["user_name"] = user[1] + " " + user[2]
            flash(f"Welcome back, {user[1]}!", "success")
            return redirect("/")
        else:
            flash("Invalid email or password. Please try again.", "error")
            return render_template("login.html")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/doctors")
def doctors():
    return render_template("doctors.html")


@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        patient   = request.form.get("patient", "").strip()
        phone     = request.form.get("phone", "").strip()
        email     = request.form.get("email", "").strip()
        doctor    = request.form.get("doctor", "").strip()
        specialty = request.form.get("specialty", "")
        date      = request.form.get("date", "")
        time_slot = request.form.get("time_slot", "")
        appt_type = request.form.get("appt_type", "in-person")
        reason    = request.form.get("reason", "")

        if patient and doctor and date:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO appointments (patient, phone, email, doctor, specialty, date, time_slot, appt_type, reason)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (patient, phone, email, doctor, specialty, date, time_slot, appt_type, reason)
            )
            conn.commit()
            conn.close()

    return render_template("appointment.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

