from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django import forms


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
  
def signup_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    # Validate user data (optional)
    # You can add validation for username, email, and password format and length

    try:
      # Create the new user
      user = User.objects.create_user(username, email, password, first_name, last_name)
      # Optionally assign user to a specific group
      # user.groups.add(group)

      # Log the user in after successful signup (optional)
      user = authenticate(request, username=username, password=password)
      if user:
        login(request, user)
        # Redirect to desired page after login (e.g., dashboard)
        return redirect('invoicing_app:dashboard')

      # Handle successful signup without auto-login
      return render(request, 'signup_success.html')  # Display success message

    except:
      # Handle potential errors during user creation (e.g., duplicate username or email)
      error_message = "There was an error creating your account. Please try again."
      return render(request, 'login/signup.html', {'error': error_message})

  else:
    # Render the signup form
    return render(request, 'login/signup.html')
