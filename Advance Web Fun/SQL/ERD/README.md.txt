# ERD Practice Assignment

## Description
This assignment represents a real-world job application system using an ERD.

## Tables
- users
- CV
- jobs
- job_dates
- applications

## Relationships
- One user has one CV
- One job has many start dates
- One user can apply to many jobs
- One job can have many applicants
- Applications table connects users and jobs

## Relationship Types Used
- One-to-One: users and cv
- One-to-Many: jobs and job_dates
- Many-to-Many: users and jobs through applications

## Notes
The `applications` table is used as a join table to connect users and jobs.
The `CV.user_id` should be unique to make sure each user has only one resume.