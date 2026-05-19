# Dojo Survey

A simple Django web application that allows users to submit a survey form and view the submitted information on a result page.

## Objectives

- Practice creating a Django project and app
- Practice working with routes in Django
- Practice handling POST requests
- Practice rendering templates with user data
- Practice using forms in Django

---

## Features

- User can enter:
  - Name
  - Dojo Location
  - Favorite Language
  - Comment
- Form data is sent using POST request
- Submitted information is displayed on a result page

---

## Technologies Used

- Python
- Django
- HTML

---

## Project Structure

```bash
dojo_survey_project/
│
├── manage.py
├── dojo_survey_project/
│
└── dojo_survey/
    ├── templates/
    │   ├── index.html
    │   └── result.html
    ├── views.py
    ├── urls.py
```

---

## Routes

| Route | Description |
|---|---|
| `/` | Display survey form |
| `/result/` | Display submitted data |

---

## How to Run

1. Clone the repository

```bash
git clone <repo-url>
```

2. Navigate to project folder

```bash
cd dojo_survey_project
```

3. Run the server

```bash
python manage.py runserver
```

4. Open browser

```text
http://127.0.0.1:8000/
```

---

## What I Learned

- Creating Django routes
- Rendering HTML templates
- Handling form submissions
- Using `request.POST`
- Passing data from views to templates

---

## Author

Jalil Wasaya