from django.db import models
# from django.contrib.auth.models import User

class People(models.Model):  # Люди в базе данных
    login = models.CharField(max_length=10)  # Логин для входа
    password = models.CharField(max_length=10)  # Пароль для входа
    name = models.CharField(max_length=100)  # Имя для документов
    email = models.CharField(max_length=20)  # Email для связи
    role = models.CharField(max_length=10)  # Роль: студент или преподаватель

class Course(models.Model):
    title = models.CharField(max_length=100)  # Название курса
    description = models.CharField(max_length=300)  # Описание курса

    def __str__(self):
        return self.title

class Assignment(models.Model):
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)  # Связь с курсом
    title = models.CharField(max_length=100)  # Название задания
    description = models.TextField()  # Описание задания

    def __str__(self):
        return f"Assignment for {self.course.title}"

