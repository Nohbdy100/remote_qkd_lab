from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# User account registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # If form is valid redirects to homepage with success message
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('core-home')
    #If there is an issue with the form remains on registration page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
