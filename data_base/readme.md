# 📘 Django Models and ORM with SQLite3 (Full Guide)

## 🔰 Introduction

Django is a powerful Python web framework that includes an Object-Relational Mapper (ORM) for interacting with databases using Python code. By default, Django uses **SQLite3**, a lightweight file-based database.

---

## 🧱 What is a Model?

A **model** in Django is a Python class that defines the structure of a database table. It is a subclass of `django.db.models.Model`.

### Example:
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

student = Student(name="John", age=20, email="john@example.com")
student.save()

Student.objects.all()           # Get all students
Student.objects.get(id=1)       # Get student by ID
Student.objects.filter(age=20)  # Filter students by age
student = Student.objects.get(id=1)
student.name = "Jane"
student.save()
student = Student.objects.get(id=1)
student.delete()