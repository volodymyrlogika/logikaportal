from django.db import models
from django.contrib.auth.models import User


class Polling(models.Model):
    # це клас який предсавляє таблицю в бд
    # Наслідується від models.Model
    STATUS_CHOICES = [
    ('active', 'Active'),
    ('completed', 'Completed'),
    ('draft', 'Draft')
    ]

    # Текст питання опитування
    question = models.CharField(max_length=2000, verbose_name="Polling Question")
    # CharField для короткого тексту max_length максимальна довжина
    # verbose_name нажва для адмінки

    # Детальний опис(не обовязковий)
    description = models.TextField(verbose_name="poll Description", blank=True)
    # TextField для великого тексту, blank=True - не обовязкове

    #  статус опитування
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='draft')
    # choices=STATUS_CHOICES обмежений з списку, default='draft' - за замовчуванням

    # дата створення та останього оновлення
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now_add=True - автоматично встановлює поточну дату з списку
    # auto_now=True - автоматично оновюється при кожному оновленні

    # автор опитування
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey - звязок багато до одного, Один User може створити багато Polling
    # on_delete=models.CASCADE - при видалені User, видаляться всі його опитування

    # час закінчення опитування(не обовязковий)
    time_limited = models.DateTimeField(null=True, blank=True, verbose_name="Time limit")
    # null=True - може бути NULL в базі
    # blank=True - може бути порожнім у формі

    # анонімно
    is_anonim = models.BooleanField(default=False, blank=True)
    # BooleanField логічне поле (True/False) blank=True - в формі може бути порожнім

    def __str__(self):
        return self.question


class Choice(models.Model):
    # до якого опитування належить варіант
    polling = models.ForeignKey(Polling, on_delete=models.CASCADE, related_name='choices')
    # ForeignKey - кожен Choice належить одному Polling
    # on_delete=models.CASCADE при видаленні Polling видаляться всі його Choice
    # related_name='choices' - як звкртатися до варіантів з опитування

    # Порядок відображення
    order = models.IntegerField(max_length=0, verbose_name="Display order", default=1)
    # Для створення варіантів (1,2,3...)

    # Текст варіанту відповіді
    text = models.CharField(max_length=500, verbose_name="Choice text")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
