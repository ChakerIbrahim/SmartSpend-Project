# Dojo & Ninjas

## Description

This project was created using Django to practice:

* Django ORM
* One-to-Many Relationships
* Foreign Keys
* Django Shell Queries
* Database Migrations

## Models

### Dojo

| Field | Type      |
| ----- | --------- |
| name  | CharField |
| city  | CharField |
| state | CharField |
| desc  | TextField |

### Ninja

| Field      | Type              |
| ---------- | ----------------- |
| first_name | CharField         |
| last_name  | CharField         |
| dojo       | ForeignKey (Dojo) |

## Relationship

A Dojo can have many Ninjas.

A Ninja belongs to one Dojo.

```python
dojo = models.ForeignKey(
    Dojo,
    related_name="ninjas",
    on_delete=models.CASCADE
)
```

## Features Completed

* Created 3 Dojos
* Deleted the 3 Dojos
* Created 3 new Dojos
* Created 9 Ninjas (3 per Dojo)
* Retrieved all Ninjas from the first Dojo
* Retrieved all Ninjas from the last Dojo
* Retrieved the last Ninja's Dojo
* Added the `desc` field to the Dojo model
* Created a new Dojo using the new field

## Technologies Used

* Python
* Django
* SQLite3

## Author

Jalil Wasaya
Murad Shaheen