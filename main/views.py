from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ForumTopic, ForumPost
from .forms import CommentForm

# Список тем
class TopicListView(LoginRequiredMixin, ListView):
    model = ForumTopic
    template_name = 'forum/topic_list.html'
    context_object_name = 'topic_list'
    ordering = ['-created_at']


# Деталі теми + коментарі
@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(ForumTopic, id=topic_id)
    posts = topic.posts.all().order_by('created_at')

    # Якщо ще немає жодного поста, створюємо перший
    if not posts.exists():
        first_post = ForumPost.objects.create(
            topic=topic,
            author=topic.created_by,
            content="Це перший пост цієї теми"
        )
        posts = topic.posts.all().order_by('created_at')

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(ForumPost, id=post_id, topic=topic)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = CommentForm()

    return render(request, 'forum/topic_detail.html', {
        'topic': topic,
        'posts': posts,
        'form': form
    })