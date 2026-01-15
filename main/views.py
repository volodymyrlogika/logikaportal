from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ForumTopic, ForumPost, Comment
from .forms import CommentForm

# Список тем
class TopicListView(LoginRequiredMixin, ListView):
    model = ForumTopic
    template_name = 'forum/topic_list.html'
    context_object_name = 'topic_list'
    ordering = ['-created_at']

# Деталі теми та коментарі
def topic_detail(request, topic_id):
    topic = get_object_or_404(ForumTopic, id=topic_id)
    posts = topic.posts.all()  # Всі пости теми
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = request.POST.get('post_id')  # Прив'язка до поста
            comment.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = CommentForm()
    
    return render(request, 'forum/topic_detail.html', {
        'topic': topic,
        'posts': posts,
        'form': form
    })
