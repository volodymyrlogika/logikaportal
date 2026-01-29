from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import ForumTopic, ForumPost, Comment, CommentReaction
from .forms import CommentForm
from django.http import HttpResponseForbidden

class TopicListView(ListView):
    model = ForumTopic
    template_name = 'forum/topic_list.html'
    context_object_name = 'topic_list'
    ordering = ['-created_at']

@login_required
def topic_detail(request, topic_id):
    topic = get_object_or_404(ForumTopic, id=topic_id)
    posts = topic.posts.all()

    if not posts.exists():
        ForumPost.objects.create(topic=topic, author=topic.created_by, content='Перший пост у темі')
        posts = topic.posts.all()

    form = CommentForm()  # завжди створюємо форму

    if request.method == 'POST':
        # Додавання коментаря
        if 'add_comment' in request.POST:
            post = get_object_or_404(ForumPost, id=request.POST.get('post_id'))
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                return redirect('topic_detail', topic_id=topic.id)

        # Реакції на коментар
        elif 'comment_reaction' in request.POST:
            comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
            reaction_type = request.POST.get('comment_reaction')
            existing_reaction = CommentReaction.objects.filter(comment=comment, user=request.user).first()

            if existing_reaction:
                if existing_reaction.reaction_type == reaction_type:
                    existing_reaction.delete()
                else:
                    existing_reaction.reaction_type = reaction_type
                    existing_reaction.save()
            else:
                CommentReaction.objects.create(comment=comment, user=request.user, reaction_type=reaction_type)

            return redirect('topic_detail', topic_id=topic.id)

    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts, 'form': form})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author != request.user and not request.user.is_staff:
        return HttpResponseForbidden("Немає прав на видалення")

    comment.delete()
    return redirect('topic_detail', topic_id=comment.post.topic.id)
