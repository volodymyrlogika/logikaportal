from django import forms
from .models import Project, UserProfile, Skill

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link', 'image'] # Поля для форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'clas': 'form-control'}) 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'location', 'website'] # Поля для форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'clas': 'form-control'})
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level'] # Поля для форми

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'clas': 'form-control'})