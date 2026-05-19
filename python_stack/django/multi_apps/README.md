# Multiple Apps

A Django project that demonstrates how to work with multiple Django applications inside one project.

This project contains three separate apps:

- Blogs App
- Surveys App
- Users App

The purpose of this assignment is to practice creating and organizing multiple Django apps and handling routes across different applications.

---

## Objectives

- Practice creating multiple Django apps
- Understand how Django projects handle multiple applications
- Practice using routes and views in different apps
- Learn how to organize large Django projects

---

## Applications Included

### Blogs App

Routes included:

| Route | Description |
|---|---|
| `/blogs` | Display all blogs |
| `/blogs/new` | Display form to create a new blog |
| `/blogs/create` | Redirect to `/blogs` |
| `/blogs/<number>` | Display a specific blog |
| `/blogs/<number>/edit` | Edit a specific blog |
| `/blogs/<number>/delete` | Delete a specific blog |

---

### Surveys App

Routes included:

| Route | Description |
|---|---|
| `/surveys` | Display all surveys |
| `/surveys/new` | Display form to create a survey |

---

### Users App

Routes included:

| Route | Description |
|---|---|
| `/register` | Create a new user |
| `/login` | User login page |
| `/users/new` | Same functionality as register |
| `/users` | Display all users |

---

## Technologies Used

- Python
- Django
- HTML

---

## Project Structure

```bash
multiple_apps_project/
│
├── manage.py
├── multiple_apps_project/
│
├── blogs/
│   ├── views.py
│   ├── urls.py
│
├── surveys/
│   ├── views.py
│   ├── urls.py
│
└── users/
    ├── views.py
    ├── urls.py
```

---

## Main Project URLs

```python
urlpatterns = [
    path('blogs/', include('blogs.urls')),
    path('surveys/', include('surveys.urls')),
    path('', include('users.urls')),
]
```

---

## How to Run

1. Navigate to the project folder

```bash
cd multiple_apps_project
```

2. Run the server

```bash
python manage.py runserver
```

3. Open browser

```text
http://127.0.0.1:8000/
```

---

## What I Learned

- Creating multiple Django apps
- Organizing routes between apps
- Using `include()` in Django URLs
- Working with dynamic URL parameters
- Redirecting between routes
- Structuring larger Django projects

---

## Author

Jalil Wasaya