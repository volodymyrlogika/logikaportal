from django import forms
from .models import ForumTopic, ForumPost




class ForumTopicForm(forms.ModelForm):
    class Meta:
        model = ForumTopic
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control mb-2'})


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control mb-2', 'rows': 4})
        