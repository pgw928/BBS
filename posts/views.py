from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment
from posts.forms   import PostForm, CommentForm

def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    context = {"posts": my_list}
    return render(request, 'list.html', context)

def p_create(request):
    # ---------------------------------
    # POST 방식으로 호출될 때
    if request.method == "POST":
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect("posts:list")

    # ---------------------------------
    # GET 방식으로 호출될 때
    else:
        post_form = PostForm()

    return render(request, "create.html", {"post_form" : post_form})
    # ---------------------------------

def p_delete(request,post_id):
    post = Post.objects.get(id = post_id)
    post.delete()

    return redirect("posts:list")

def p_upgrade(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    # ---------------------------------
    # POST 방식으로 호출될 때
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post_form.save()
            return redirect("posts:list")

    # ---------------------------------
    # GET 방식으로 호출될 때
    else:
        post_form = PostForm(instance = post)

    return render(request, "create.html", {"post_form" : post_form})
    # ---------------------------------

def p_read(request,post_id):
    my_list = get_object_or_404(Post,id=post_id)
    context ={"post" : my_list}
    return render(request, "read.html",context)


def p_comment(request,post_id):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = Post.objects.get(pk=post_id)
            comment_form.save()
            return redirect("posts:read", post_id)

    # ---------------------------------
    # GET 방식으로 호출될 때
    else:
        comment_form = CommentForm()

    return render(request, "comment.html", {"comment_form" : comment_form})
    # ---------------------------------

def c_delete(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    # comment = Comment.objects.get(id=comment_id)
    post_id = comment.post_id
    comment.delete()
    return redirect("posts:read", post_id)

def c_upgrade(request,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post_id
    # ---------------------------------
    # POST 방식으로 호출될 때
    if request.method == "POST":
        comment_form = CommentForm(request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            return redirect("posts:read", post_id)

    # ---------------------------------
    # GET 방식으로 호출될 때
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, "comment.html", {"comment_form": comment_form})
    # ---------------------------------



