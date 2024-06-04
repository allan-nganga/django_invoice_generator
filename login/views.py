from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

# Display login page
class LoginView(LoginView):
    template_name = 'registration/login.html'

# Function for Authentication
def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login:login')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})