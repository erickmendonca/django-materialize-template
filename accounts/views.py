from django.contrib.auth.decorators import login_required
from django.shortcuts import render, resolve_url


def change_language(request):
    context = {
        'title': 'Set Language!',
        'redirect_to': resolve_url('/')
    }
    return render(request, 'accounts/change_language.html', context)


@login_required
def profile(request):
    context = {
        'title': 'User Profile',
        'user': request.user
    }
    return render(request, 'accounts/profile.html', context)
