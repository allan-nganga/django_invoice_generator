from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username', max_length=254)

def login(request):
  if request.method == 'POST':
        form = EmailOrUsernameAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('invoicing_app:dashboard')  # Redirect to a success page.
  else:
      form = EmailOrUsernameAuthenticationForm()
  return render(request, 'registration/login.html', {'form': form})
  
def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.email = form.cleaned_data.get('email')
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user.username, password=raw_password)
        if user is not None:
          login(request, user)
          return redirect('invoicing_app:dashboard')
    else:
        return render(request, 'registration/signup.html', {'form':form, 'error':True})
  else:
      form = SignUpForm()
  return render(request, 'registration/signup.html', {'form': form, 'error':False})


"""
@login_required    
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # Update the session to reflect the new password
            return redirect('settings/profile_info.html')
        else:
            form = PasswordChangeForm(request.user)
        context = {
            'form':form,
        }
        return render(request, 'settings/edit_profile.html', context)
        """