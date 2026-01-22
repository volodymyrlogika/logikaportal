from django.contrib import admin
from django.utils.html import format_html

from .models import UserProfile, Skill, Project



class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "avatar_preview",
        "location",
        "created_at",
    )

    list_select_related = ("user",)
    search_fields = (
        "user__username",
        "user__email",
        "location",
    )

    list_filter = ("created_at",)
    ordering = ("-created_at",)

    readonly_fields = ("created_at", "avatar_preview")

    fieldsets = (
        ("Користувач", {
            "fields": ("user",)
        }),
        ("Профіль", {
            "fields": ("avatar", "avatar_preview", "bio", "location", "website")
        }),
        ("Системна інформація", {
            "fields": ("created_at",)
        }),
    )

    inlines = [SkillInline, ProjectInline]

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:50%;" />',
                obj.avatar.url
            )
        return "—"

    avatar_preview.short_description = "Avatar"



@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "profile",
    )

    search_fields = (
        "name",
        "profile__user__username",
    )

    list_filter = ("level",)
    ordering = ("-level",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "profile",
        "created_at",
    )

    search_fields = (
        "title",
        "profile__user__username",
    )

    list_filter = ("created_at",)
    ordering = ("-created_at",)

    readonly_fields = ("created_at",)

