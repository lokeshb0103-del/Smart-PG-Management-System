# Smart PG Management System

A Python-based Smart PG (Paying Guest) Management System developed to simplify the management of PG accommodations. This application helps administrators manage tenants, rooms, rent payments, complaints, visitors, and reports through an easy-to-use interface.

---

# Project Overview

The Smart PG Management System is designed to automate daily PG management tasks. It minimizes manual work, improves record management, and provides quick access to important information such as room allocation, tenant details, rent status, and visitor records.

---

# Features

## Authentication
- Admin Login
- Secure User Authentication

## Room Management
- Add New Rooms
- Update Room Details
- Delete Rooms
- Check Room Availability

## Tenant Management
- Add Tenant Details
- Update Tenant Information
- Delete Tenant Records
- Assign Rooms

## Rent Management
- Record Monthly Rent
- Update Payment Status
- View Payment History

## Complaint Management
- Register Complaints
- Update Complaint Status
- View Complaint Records

## Visitor Management
- Add Visitor Details
- Maintain Visitor Log
- Track Entry Information

## Reports
- Generate Tenant Reports
- Room Occupancy Reports
- Rent Reports
- Complaint Reports

---

# Technologies Used

## Programming Language
- Python

## Database
- MySQL

## GUI
- Tkinter

## Development Tool
- Visual Studio Code

---

# Project Structure

```
Smart-PG-Management-System/
│
├── __pycache__/                 # Python cache files
│
├── login.py                     # User/Admin Login Module
│
├── main.py                      # Main Application Entry Point
│
├── room.py                      # Room Management Module
│
├── tenant.py                    # Tenant Management Module
│
├── rent.py                      # Rent Management Module
│
├── complaint.py                 # Complaint Management Module
│
├── visitor.py                   # Visitor Management Module
│
├── report.py                    # Report Generation Module
│
└── README.md
```

---

# File Description

### main.py
Acts as the main entry point of the application. It connects all modules and displays the main dashboard.

### login.py
Handles user authentication and validates login credentials before granting access to the system.

### room.py
Manages room-related operations such as:
- Add Room
- Update Room
- Delete Room
- View Room Details
- Check Availability

### tenant.py
Manages tenant information including:
- Add Tenant
- Update Tenant
- Delete Tenant
- View Tenant Records

### rent.py
Handles rent-related activities:
- Record Monthly Rent
- Update Payment Status
- View Rent History

### complaint.py
Allows management of complaints:
- Register Complaint
- Update Complaint Status
- View Complaints

### visitor.py
Maintains visitor information:
- Visitor Registration
- Visitor Records
- Entry Details

### report.py
Generates reports for:
- Rooms
- Tenants
- Rent Collection
- Complaints
- Visitors

---

# Installation

## Step 1

Clone the repository

```bash
git clone https://github.com/yourusername/Smart-PG-Management-System.git
```

## Step 2

Move into the project directory

```bash
cd Smart-PG-Management-System
```

## Step 3

Install required libraries

```bash
pip install mysql-connector-python
```

If using additional packages:

```bash
pip install -r requirements.txt
```

---

# Database Setup

1. Install MySQL.
2. Create a database.

Example:

```sql
CREATE DATABASE smart_pg;
```

3. Create required tables:
- login
- room
- tenant
- rent
- complaint
- visitor

4. Update database credentials inside the project.

Example:

```python
host="localhost"
user="root"
password="your_password"
database="smart_pg"
```

---

# Running the Project

Execute the following command:

```bash
python main.py
```

The application will start, displaying the login page.

---

# Modules

- Login
- Dashboard
- Room Management
- Tenant Management
- Rent Management
- Complaint Management
- Visitor Management
- Reports

---

# Future Enhancements

- Online Rent Payment
- Email Notifications
- SMS Alerts
- QR Code Visitor Entry
- Mobile Application
- Biometric Attendance
- Cloud Database
- Analytics Dashboard

---

# Advantages

- Easy to Use
- User-Friendly Interface
- Secure Login
- Centralized Data Management
- Reduced Manual Work
- Faster Record Retrieval
- Better Complaint Tracking
- Efficient Rent Monitoring

---

# System Requirements

## Hardware

- Processor: Intel i3 or above
- RAM: 4 GB Minimum
- Storage: 500 MB Free Space

## Software

- Windows 10/11
- Python 3.10+
- MySQL Server
- Visual Studio Code

---

# Author

**Lokesh Bodavula**

B.Tech – Computer Science and Engineering (Artificial Intelligence)

---

# License

This project is developed for educational purposes only.
