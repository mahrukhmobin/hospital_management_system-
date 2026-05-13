# Hospital Management System

A Python-based desktop Hospital Management System with role-based access for admins and patients, built using PyQt6 and SQLite.

---

## Project Overview

This system modernizes hospital workflows by digitizing patient records, appointment booking, doctor schedules, and email notifications — all through a clean GUI application.

---

## Features

**Admin Module**
- Secure admin login
- View and manage all patient records from database
- Doctor schedule management
- Patient medical history lookup by CNIC
- Send appointment confirmation emails directly from the system
- View hospital-wide patient and doctor statistics

**Patient Module**
- Patient login and account creation
- Appointment booking form with department selection
- Doctor schedule viewer
- Patient history access

**General**
- Role-based access control (Admin / Patient)
- SQLite database for persistent patient and doctor records
- Automated email notifications for appointment confirmations
- 20 pre-loaded patient history reports
- Clean and intuitive GUI built with PyQt6

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| PyQt6 | Desktop GUI |
| SQLite | Database for patient and doctor records |
| smtplib | Email notifications |
| JSON | Appointment data storage |

---

## Project Structure

```
hospital-management-system/
│
├── HMS_PROJECT.py              # Main entry point
├── mainpage.py                 # Home screen UI
├── login_page.py               # Login UI
├── create_account.py           # Account creation UI
├── admin_dashboard.py          # Admin dashboard UI
├── dashboard_for_patients.py   # Patient dashboard UI
├── patient_appoint_form.py     # Appointment form UI
├── pat_app_to_mail.py          # Appointment to email handler
├── pat_his_log.py              # Patient history login UI
├── history_show.py             # Patient history viewer
├── ad_pat_record.py            # Admin patient records
├── ad_pat_login.py             # Admin patient login
├── ad_doc_sch.py               # Admin doctor schedule
├── pat_doc_sch.py              # Patient doctor schedule
├── mailing.py                  # Email sending module
├── send_email.py               # Email UI handler
├── report_history1o.py         # Patient report files
├── report_history2-20.py       # (20 patient history reports)
├── hospital.db                 # SQLite database
└── README.md
```

---

## Note

This repository contains the Python source files only. The `.ui` files (PyQt6 designer files) and image assets are not included as they were part of a collaborative project.

---

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/mahrukhmobin/hospital-management-system.git

# 2. Install dependencies
pip install PyQt6

# 3. Add your email credentials in mailing.py and send_email.py
# Replace placeholder email and password with your own

# 4. Run the application
python HMS_PROJECT.py
```

---


## Team

| Member | 
|--------|
| Mahrukh Mobin |
| Mahnoor Baloch |
| Fizza Fatima |
| Zoya Rabail |

---

*Built by [Mahrukh Mobin](https://github.com/mahrukhmobin) — Computer Engineering Student @ UET Lahore*
