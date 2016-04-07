from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from .forms import PostForm
from .models import Profile
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def post_detail(request, pk):
    post = get_object_or_404(Profile, pk=pk)
    return render(request, 'users/detail.html', {'detail': post})

def logout_view(request):
    logout(request)
    return redirect('login_user')

def login_user(request):
    state = "Please login"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                detail = Profile.objects.get(owner = user)
                return redirect('post_detail', pk=detail.pk)
               # return render(request, "users/detail.html", {'detail': detail})
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('users/auth.html',{'state':state, 'username': username})



def detail_edit(request, pk):
    post = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'users/detail_edit.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_user')
            #return HttpResponseRedirect('users/register_success')
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('users/register.html', args)






