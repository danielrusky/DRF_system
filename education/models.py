from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    image = models.ImageField(upload_to='courses/', verbose_name='Изображение курса', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока')
    image = models.ImageField(upload_to='courses/lessons/', verbose_name='Изображение урока', **NULLABLE)
    link = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return f"{self.course} - {self.title}"

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
