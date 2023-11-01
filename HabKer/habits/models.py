from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from model_utils import Choices
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
import mptt

User = get_user_model()


class HabitModel(models.Model):

    DURATION = Choices("DAILY", "WEEKLY", "MONTHLY")

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=255, choices=DURATION, default=DURATION.DAILY)
    completed = models.BooleanField(default=False)
    start_at = models.DateField()
    finish_at = models.DateField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('habit_detail', kwargs={'pk': self.pk})


class TaskModel(models.Model):
    habit = models.ForeignKey(HabitModel, on_delete=models.CASCADE)
    task_date = models.DateField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} task {self.habit.title}'

    class Meta:
        ordering = ['task_date']