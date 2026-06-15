# 💰 Smart Household Expense Manager

A web-based financial management platform that helps individuals and families track expenses, manage budgets, and stay on top of bill payments.

## 📖 Overview

Smart Household Expense Manager is designed to simplify personal and household financial planning. Users can record daily expenses, create budgets, receive bill reminders, and monitor spending habits through an easy-to-use interface.

The platform provides a centralized solution for managing financial activities and encourages better budgeting and saving practices.

---

## 🚀 Features

### 👤 User Management
- User registration and login
- Secure authentication system
- User profile customization
- Email verification support

### 💸 Expense Tracking
- Add, edit, and delete expenses
- Categorize expenses
- Track spending history
- View expense records by date

### 📊 Budget Management
- Create monthly budgets
- Set category-specific spending limits
- Compare expenses against budgets
- Monitor remaining budget

### 🔔 Bill Reminders
- Create bill reminders
- Track due dates
- Mark bills as paid
- Prevent missed payments

### ⚙️ User Preferences
- Preferred currency selection
- Language preferences
- Personalized user settings

---

## 🛠️ Technologies Used

### Backend
- Python
- Django

### Database
- SQLite3

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Authentication
- Django Authentication System
- Django AllAuth

---

## 📂 Database Structure

### Expense
Stores user expenses.

| Field | Description |
|---------|-------------|
| title | Expense title |
| amount | Expense amount |
| category | Expense category |
| date | Expense date |
| user | Expense owner |

### Budget
Stores user budgets.

| Field | Description |
|---------|-------------|
| income | Monthly income |
| category | Budget category |
| budget_amount | Budget limit |
| user | Budget owner |

### Bill Reminder
Stores upcoming bills.

| Field | Description |
|---------|-------------|
| name | Bill name |
| amount | Bill amount |
| due_date | Due date |
| is_paid | Payment status |
| user | Bill owner |

### User Profile
Stores user preferences.

| Field | Description |
|---------|-------------|
| currency | Preferred currency |
| language | Preferred language |
| user | Linked user |

---

## 📋 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/smart-household-expense-manager.git
cd smart-household-expense-manager
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Start Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

---

## 🎯 Future Improvements

- Data visualization charts
- Export reports to PDF
- Multi-family accounts
- Mobile responsive dashboard
- SMS and email bill notifications
- AI-powered spending analysis
- Savings goals tracker

---

## 📸 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Expense Management
![Expenses](screenshots/expenses.png)


### Bill Reminders
![Reminders](screenshots/reminders.png)
---

## 👥 Team Members

- Chaker Ibrahim
- Jalil Wasaya
- Husni Ahmad
- Aws Sleebi

---

## 📄 License

This project was developed for educational purposes as part of a Full Stack Development Bootcamp.

---

## 🙏 Acknowledgements

- Django Documentation
- Django AllAuth
- Bootstrap
- Open Source Community
