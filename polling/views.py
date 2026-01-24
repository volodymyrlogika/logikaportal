from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Polling, Choice
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import F # Імпортуємо F expression


class PollingListView(ListView):
    model = Polling
    template_name = 'polling_list.html'
    context_object_name = 'polling_list'
    ordering = ['created_at']


class PollingDetailView(DetailView):
    model = Polling
    template_name = 'polling/polling_detail.html'
    context_object_name = 'polling'

    def post(self, request, *args, **kwargs):
        polling = self.get_object()
        try:
            # Намагаємося знайти обраний варіант за ID з POST-запиту
            selected_choice = polling.choices.get(pk=request.POST.get('choice'))
        except (KeyError, Choice.DoesNotExist):
            # Якщо варіант не обрано або його не існує:
            # Повертаємо форму голосування зі сповіщенням про помилку
            return render(request, self.template_name, {
                'polling': polling,
                'error_message': "Ви не обрали жодного варіанту відповіді.",
            })
        else:
            # *** Зберігаємо голос за допомогою F expression ***
            # Атомарно збільшуємо лічильник голосів на 1
            selected_choice.votes = F('votes')+1
            selected_choice.save()

            # ***Перенаправляємо користувача***
            # Використовуємо HttpResponseRedirect, щоб запобігти повторному надсиланню форми
            # Перенаправляємо на сторінку результатів
            # Приклад нижче редиректить на ту ж сторінку деталей, але в майбутньому варто додати сторінку результатів.
            return HttpResponseRedirect(reverse('polling_detail', args=(polling.id,)))