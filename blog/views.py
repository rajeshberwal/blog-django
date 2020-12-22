import django
from django.core import paginator
from django.core.checks import messages
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# We have replace this view with our classed based view PostListView
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 3) # 3 posts in per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer we are goign to set it to 1
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range we are going to deliver the last page
        posts = paginator.page(paginator.num_pages)
    
    return render(request,
                    'blog/post/list.html',
                    {
                        'page': page,
                        'posts': posts                
                    })


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                            slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    
    # all the active comments
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # comment get posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # creating comment object and not saving in database
            new_comment = comment_form.save(commit=False)

            # assigning the current post to comment
            new_comment.post = post

            # saving the comment to databse
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                    'blog/post/detail.html',
                    {
                        'post': post,
                        'comments': comments,
                        'new_comment': new_comment,
                        'comment_form': comment_form
                    })


def post_share(request, post_id):
    # retrive post usign id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # forms was submitted
        form = EmailPostForm(request.POST)

        if form.is_valid():
            # forms validated
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recomends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            messages = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, messages, 'rajesh.umedberwal@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})