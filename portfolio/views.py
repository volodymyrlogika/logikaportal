
#! додати view де можна подивитись всі проекти
#! додати сторінки для додавання, редагування, перегляду проектів

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import UserProfile, Skill, Project
from .forms import UserProfileForm, SkillForm, ProjectForm


def profile_detail(request, username):
    profile = get_object_or_404(UserProfile, user__username=username)

    context = {
        "profile": profile,
        "skills": profile.skills.all(),
        "projects": profile.projects.all(),
    }

    return render(request, "portfolio/profile_detail.html", context)


@login_required
def profile_edit(request):
    profile = request.user.profile

    if request.method == "POST":
        form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            return redirect(
                "profile_detail",
                username=request.user.username
            )
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "portfolio/profile_edit.html", {"form": form})


@login_required
def skill_add(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.profile = request.user.profile
            skill.save()
            return redirect(
                "profile_detail",
                username=request.user.username
            )
    else:
        form = SkillForm()

    return render(request, "skills/form.html", {"form": form})


@login_required
def skill_edit(request, pk):
    skill = get_object_or_404(
        Skill,
        pk=pk,
        profile=request.user.profile
    )

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect(
                "profile_detail",
                username=request.user.username
            )
    else:
        form = SkillForm(instance=skill)

    return render(request, "skills/form.html", {"form": form})


@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(
        Skill,
        pk=pk,
        profile=request.user.profile
    )
    skill.delete()

    return redirect(
        "profile_detail",
        username=request.user.username
    )


@login_required
def project_add(request):
    if request.method == "POST":
        form = ProjectForm(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user.profile
            project.save()
            return redirect(
                "profile_detail",
                username=request.user.username
            )
    else:
        form = ProjectForm()

    return render(request, "projects/form.html", {"form": form})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    return render(
        request,
        "projects/detail.html",
        {"project": project}
    )


@login_required
def project_edit(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk,
        profile=request.user.profile
    )

    if request.method == "POST":
        form = ProjectForm(
            request.POST,
            request.FILES,
            instance=project
        )
        if form.is_valid():
            form.save()
            return redirect(
                "profile_detail",
                username=request.user.username
            )
    else:
        form = ProjectForm(instance=project)

    return render(request, "projects/form.html", {"form": form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(
        Project,
        pk=pk,
        profile=request.user.profile
    )
    project.delete()

    return redirect(
        "profile_detail",
        username=request.user.username
    )

def project_list(request, username):
    profile = get_object_or_404(UserProfile, user__username=username)
    projects = profile.projects.all()

    return render(
        request,
        "portfolio/user_projects.html",
        {
            "profile": profile,
            "projects": projects
        }
    )

def project_list(request):
    projects = Project.objects.select_related("profile", "profile__user")

    return render(
        request,
        "projects/projects_list.html",
        {"projects": projects}
    )
