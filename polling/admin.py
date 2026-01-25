from django.contrib import admin
from .models import Polling, Choice

# Створюємо клас Inline для моделі Choice
class ChoiceInline(admin.TabularInline): # TabularInline відображає варіанти у вигляді таблиці
    model = Choice
    extra = 3 # Додає 3 порожні форми для варіантів за замовчуванням
    fields = ['text']# Поля, які будуть відображатися
    readonly_fields = ['votes']  # Робимо поле votes тільки для читання в адмінці

# Реєструємо модель Polling і додаємо до неї наш інлайн
class PollingAdmin(admin.ModelAdmin):
    list_display = ('question', 'status', 'created_at', 'author')
    list_filter = ('status', 'created_at')
    search_fields = ('question', 'description')
    fieldsets = [
        (None, {'fields': ['question', 'description', 'status', 'author']}),
        ('Додаткова інформація', {'fields': ['time_limited', 'is_anonim'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # Додаємо інлайн сюди


admin.site.register(Polling, PollingAdmin)
# Тепер Choice будет керуватися через PollingAdmin, цей рядок можна вдалити або закоментувати:
# admin.site.register(Choice)1
