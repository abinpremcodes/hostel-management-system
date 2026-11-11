# Hostel Management System

A web-based hostel management application built with Django to simplify hostel administration and student services through a centralized platform.

## Live Demo

**Website:** https://hostel-management-system-r1pe.onrender.com

### Demo Admin Login

- **Username:** `demo_admin`
- **Password:** 'demoabin'

*Note: This is an application-level admin account, not a Django superuser. Demo student credentials will be added after creating the student account.*

## Overview

The Hostel Management System helps administrators and wardens manage hostel operations, while students can access their personal hostel information and services through a dedicated dashboard.

## Features

### Student Management
- Manage student accounts and profiles.
- View student information and hostel details.
- Provide students with access to their personal dashboard.

### Hostel Management
- Manage hostel buildings and floors.
- Manage rooms, beds, and room availability.
- Handle student room allocations.

### Attendance Management
- Record and manage student attendance.
- View attendance records with date-based filtering.

### Fee Management
- Manage hostel fee records.
- Allow students to view their fee information.

### Complaint Management
- Submit and manage hostel complaints.
- Track complaint status and priority.
- Support administrative complaint handling.

### Visitor Management
- Record and manage visitor information.
- Allow students to view their visitor records.

### Dashboard
- Separate dashboards for administrators and students.
- Display relevant hostel information and management summaries.
- Visualize key information using charts.

## Technology Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Charts:** Chart.js
- **Icons:** Bootstrap Icons

## Getting Started

### Prerequisites

Make sure you have installed:

- Python
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone https://github.com/abinpremcodes/hostel-management-system.git
cd hostel-management-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure the Django secret key, debug setting, and PostgreSQL database credentials according to your project's settings.

**Important:** Keep `.env` out of GitHub. Never publish real passwords or secret keys.

### 5. Create the PostgreSQL database

Create a PostgreSQL database using the name configured in your environment variables.

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your account.

### 8. Run the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## Project Structure

```text
Hostel_Management_System/
├── accounts/
├── allocations/
├── attendance/
├── complaints/
├── dashboard/
├── events/
├── fees/
├── hostel/
├── visitors/
├── config/
├── templates/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Security Notes

- Keep secret keys and database credentials in environment variables.
- Do not commit `.env` files or database backups containing private information.
- Use `DEBUG=False` and configure `ALLOWED_HOSTS` appropriately before production deployment.
- Use HTTPS and secure production settings when deploying the application.
- Demo credentials are public and should never be reused for personal accounts.

## Future Improvements

- Student vacate requests.
- In-app notifications.
- Payment receipt generation.
- Automated fee reminders.

## Author

**Abin Prem**

- GitHub: [abinpremcodes](https://github.com/abinpremcodes)
- LinkedIn: [Abin Prem](https://www.linkedin.com/in/abin-prem-t/)

---

Developed as a Django-based hostel management project.
