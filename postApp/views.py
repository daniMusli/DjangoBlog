from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import post
from .forms import postForm,commentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def post_index(request):
    posts_list = post.objects.all()

    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains = query)|
            Q(content__icontains = query)|
            Q(user__first_name__icontains = query)|
            Q(user__last_name__icontains = query)
        ).distinct()

    paginator = Paginator(posts_list, 5) # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request,'postsFiles/index.html',{'posts':posts})


def post_detail(request,postsSlug):
    birpost = get_object_or_404(post,slug = postsSlug)

    form = commentForm(request.POST or None)
    if form.is_valid():
        savedComment = form.save(commit=False)
        savedComment.yorum = birpost
        savedComment.save()
        return HttpResponseRedirect(birpost.get_absolute_url())

    context={
        'birpost':birpost,
        'comform':form,
    }
    return render(request,'postsFiles/details.html',context)

def post_create(request):

    if not request.user.is_authenticated():
        return Http404()

    form = postForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        savedPost = form.save(commit=False)
        savedPost.user = request.user
        savedPost.save()
        messages.success(request,"başarılı oluşturuldu")
        return HttpResponseRedirect(savedPost.get_absolute_url())

    context={'form':form}
    return render(request,'postsFiles/create.html',context)


def post_update(request,postsSlug):
    if not request.user.is_authenticated():
        return Http404()

    updatePost = get_object_or_404(post,slug=postsSlug)
    form = postForm(request.POST or None , request.FILES or None ,instance=updatePost)

    if form.is_valid():
        form.save()
        messages.success(request,"başarılı Güncellenmiş")
        return HttpResponseRedirect(updatePost.get_absolute_url())

    context={'form':form}
    return render(request,'postsFiles/create.html',context)


def post_delete(request,postsSlug):
    if not request.user.is_authenticated():
        return Http404()

    deletePost = get_object_or_404(post , slug=postsSlug)
    deletePost.delete()
    messages.success(request,"başarılı silinmiş")
    return redirect('post:index')


