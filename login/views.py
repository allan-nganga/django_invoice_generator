from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
  if request.method == 'POST':
    email = request.POST.get('email')  # Handle potential absence of 'email' key
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user:
      login(request, user)
      return redirect('invoicing_app:dashboard')  # Replace with actual dashboard URL name
    else:
      # Invalid credentials, display error message
      return render(request, 'login/login.html', {'error': 'Invalid email address or password'})
  else:
    # Render the login form
    return render(request, 'login/login.html')
  
def signup_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

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
        return redirect('invoicing_app:dashboard')  # Replace with your actual URL name

      # Handle successful signup without auto-login
      return render(request, 'signup_success.html')  # Display success message

    except:
      # Handle potential errors during user creation (e.g., duplicate username or email)
      error_message = "There was an error creating your account. Please try again."
      return render(request, 'login/signup.html', {'error': error_message})

  else:
    # Render the signup form
    return render(request, 'login/signup.html')
