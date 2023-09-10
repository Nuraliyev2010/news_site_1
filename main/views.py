from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()
@login_required(login_url='login_url')
def index_view(request):
    context = {
        "banner": Banner.objects.all().order_by('-id')[:2],
        "restaurent": Restaurent.objects.all(),
        "special_menu": Special_menu.objects.all().order_by('-id')[:4],
        "menu": Menu.objects.all().order_by('-id')[:8],
        "testiminional": Testiminional.objects.all().order_by('-id')[:3],
        "blog": Blog.objects.all().order_by('-id')[:2],
    }
    return render(request, 'index.html',context)

@login_required(login_url='login_url')
def about_view(request):
    context = {
        "restaurent": Restaurent.objects.all(),
        "chefs": Chefs.objects.all()
    }
    return render(request, 'about.html',context)

@login_required(login_url='login_url')
def news_view(request):
    context = {
        "blog": Blog.objects.all()
    }
    return render(request, 'news.html',context)

@login_required(login_url='login_url')
def service_view(request):
    context = {
        "menu": Menu.objects.all().order_by('-id')[:8],
    }
    return render(request, 'services.html',context)


@login_required(login_url='login_url')
def recipes_view(request):
    context = {
        "menu": Menu.objects.all().order_by('-id')[:8],
    }
    return render(request, 'recipes.html',context)

@login_required(login_url='login_url')
def delete_blog_view(request, pk):
    new = News.objects.get(pk=pk)
    new.delete()
    return redirect('index_url')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request,usr)
            return redirect('index_url')
    return render(request, 'login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(
            username=username,
            password=password,
        )
        return redirect('index_url')
    return render(request, 'log-up.html')

@login_required(login_url='login_url')
def logout_view(request):
    logout(request)
    return redirect('signup_url')



@login_required(login_url='login_url')
def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)




@login_required(login_url='login_url')
def delete_user_view(request, pk):
    user= User.objects.get(pk=pk)
    user.delete()
    return redirect('signup_url')

@login_required(login_url='login_url')
def update_blog_view(request, pk):
    new = News.objects.get(pk=pk)
    if request.method == "POST":
        title = request.POST['title']
        img = request.FILES.get('img')
        category = request.POST['category']
        date = request.POST['date']
        text = request.POST['text']
        new.title = title
        new.category_id = category
        new.date = date
        new.text = text
        if img is not None:
            new.img = img
        new.save()
        return redirect('single_url', new.id)
    context = {
        'category': Category.objects.all(),
        'new':new
    }
    return render(request, 'update-blog.html',context)
@login_required(login_url='login_url')
def single_view(request, pk):
    new = News.objects.get(pk=pk)
    context ={
        'new' : new,
        'category': Category.objects.all(),
    }
    return render(request, 'single-post.html', context)

@login_required(login_url='login_url')
def search_view(request):
    title = request.GET.get('search')
    context={
        's_news': News.objects.filter(title__icontains=title),
        'category': Category.objects.all(),
    }
    return render(request, 'seacrh.html', context)



def edit_user_view(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        username = rquest.POST['username']
        email = request.POST.get('email')
        img = request.FILES.get('img')
        bio = request.POST.get('bio')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        coniform_password = request.POST.get('coniform_password')
        user = username = username
        user.email = email
        user.bio = bio
        if img is not None:
            user.photo = img
            if new_password == coniform_password:
                user.set_password(new_password)
            user.save()
            return redirect("profile_url",user.pk)
        context = {
            'user':user
        }
        return render(request,'edit-user.html',context)