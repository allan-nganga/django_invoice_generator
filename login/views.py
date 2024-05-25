from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Display login page
class LoginView(LoginView):
    template_name = 'registration/login.html'

# Dashboard function
@login_required
def dashboard(request):
    return render(request, 'invoice/dashboard.html')

def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login:login')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form":form})