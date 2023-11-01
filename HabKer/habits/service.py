from datetime import datetime
from .models import *


def get_days_count(start_at, finish_at):
    start, finish = str(start_at).replace('-', '/'), str(finish_at).replace('-', '/')

    d1, d2 = datetime.strptime(start, "%Y/%m/%d"), datetime.strptime(finish, "%Y/%m/%d")
    count = d2.date() - d1.date()

    return d1.date(), d2.date(), count


def get_prof_data(data):
    start_at = data.get('start_at')
    finish_at = data.get('finish_at')
    duration = data.get('duration')
    title = data.get('title')
    description = data.get('description')

    return title, start_at, finish_at, duration, description


class Habit:

    def __init__(self, title, start_at, finish_at, duration, description, user):
        self.start_at = start_at
        self.finish_at = finish_at
        self.duration = duration
        self.title = title
        self.description = description
        self.user = user

    def create_new_habit(self):
        habit = HabitModel(
            title=self.title,
            description=self.description,
            start_at=self.start_at,
            finish_at=self.finish_at,
            duration=self.duration,
            user=self.user
        )

        return habit

