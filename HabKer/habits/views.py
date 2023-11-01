import datetime
from datetime import timedelta
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from .forms import HabitForm
from .service import *
from .models import *


class NewHabitView(View):
    @staticmethod
    def get(request):
        form = HabitForm()

        return render(request, 'habits/newhabit.html', {'form': form})

    def post(self, request):
        data = request.POST

        title, start_at, finish_at, duration, description = get_prof_data(data)
        user = self.request.user

        habit = Habit(
            title=title,
            start_at=start_at,
            finish_at=finish_at,
            duration=duration,
            description=description,
            user=user
        )
        habit = habit.create_new_habit()
        habit.save()

        d1, d2, count = get_days_count(start_at, finish_at)

        while d1 <= d2:
            task = TaskModel(habit=habit, task_date=d1)
            task.save()
            d1 = d1 + timedelta(days=1)

        return redirect('index')


class HabitDetail(DetailView):
    model = HabitModel
    template_name = 'habits/habitdetail.html'
    context_object_name = 'Habit'


class Index(View):

    @staticmethod
    def get(request):
        habits = HabitModel.objects.filter(completed=False, user=request.user)
        date = datetime.now().date()
        user = request.user

        tasks = []

        for i in habits:
            task = i.taskmodel_set.filter(task_date=date)
            if task:
                task = task[0]
                tasks.append(task)

        return render(request, 'habits/index.html', {'habits': habits, 'tasks': tasks, 'date': date, 'user': user})


class Complete(View):

    @staticmethod
    def get(request):
        data = request.GET

        task = TaskModel.objects.get(pk=data.get('pk'))
        task.done = True
        task.save()


class Profile(View):

    @staticmethod
    def get(request, pk):
        user = User.objects.get(pk=pk)
        habits = HabitModel.objects.filter(user=user)
        tasks = []

        for i in habits:
            task = i.taskmodel_set.all().order_by('task_date')
            if task:
                task = task[0]
                tasks.append(task)

        context = {
            'user': user,
            'habits': habits,
            'tasks': tasks,
        }

        return render(request, 'habits/profile.html', context)