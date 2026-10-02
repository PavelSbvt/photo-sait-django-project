# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment
from .models import Post

@login_required # Делает так, что лайкнуть может только залогиненный пользователь
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)

    # Проверяем, лайкнул ли пользователь этот пост уже
    if post.likes.filter(id=request.user.id).exists():
        # Если да — убираем лайк
        post.likes.remove(request.user)
    else:
        # Если нет — добавляем
        post.likes.add(request.user)

    # После обработки перенаправляем пользователя обратно на ту же страницу
    return redirect('post_detail', pk=pk)

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/post_detail.html', {
#         'post': post,
#         'comments': comments,
#         'form': form
#     })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(author=cd['author'], text=cd['text'], post=post)
            return redirect('post_detail', pk=post.pk)
    else: form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        # Получаем файл из request.FILES
        # 'image' — это значение атрибута name="image" в вашем HTML-инпуте
        image = request.FILES.get('image')
        post = Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            image=image
        )
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog/create_post.html')

def index(request):
    return render(request, 'blog/index.html')
# def base(request):
#     return render(request, 'blog/base.html')
def base(request):
    return render(request, 'blog/base.html')

from django.db.models import Count

def post_list(request):
    posts = Post.objects.annotate(
        comments_count=Count('comments')
    ).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})