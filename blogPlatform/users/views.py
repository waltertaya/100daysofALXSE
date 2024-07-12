from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', { 'form': form })


@login_required
def profile(request):
    return render(request, 'users/profile.html')
