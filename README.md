# Hotel-Management-System

---

# 🏨 Hotel Management System

A simple **Hotel Management System** built using **Python** and **MySQL**, designed to efficiently handle hotel operations like room booking, customer management, and record maintenance.

---

## 📌 Features

* Create and manage hotel database with MySQL.
* Add, update, and delete customer records.
* Manage room availability and bookings.
* Store guest details securely in the database.
* User-friendly console-based interface.
* Prevents duplicate entries and ensures data consistency.

---

## 🛠️ Technologies Used

* **Python** – for application logic
* **MySQL** – for database management
* **mysql-connector-python** – to connect Python with MySQL

---

## 📂 Project Structure

```
Hotel_Management_System/
│-- hotel_management.py   # Main Python script
│-- requirements.txt      # Required dependencies
│-- README.md             # Project Documentation
```

---

## ⚙️ Installation & Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/Hotel_Management_System.git
   ```

2. Navigate into the project folder:

   ```bash
   cd Hotel_Management_System
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Setup MySQL database:

   ```sql
   create database HOTEL_MANAGEMENT;
   use HOTEL_MANAGEMENT;
   ```

5. Run the project:

   ```bash
   python hotel_management.py
   ```

---

## 📊 Database Schema

**Table: hotel**

* `id` (INT, Primary Key, Auto Increment)
* `name` (VARCHAR) – Guest name
* `phone` (VARCHAR) – Contact number
* `room_no` (INT) – Room assigned
* `days` (INT) – Duration of stay
* `bill` (FLOAT) – Calculated bill amount

---

## 🚀 Future Scope

* Add GUI interface using **Tkinter** or **PyQt**.
* Implement **online booking system** with login authentication.
* Add **payment gateway integration**.
* Create **reports & analytics dashboards** for hotel admins.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and create a pull request.

---
