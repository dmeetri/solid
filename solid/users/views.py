from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect

class SolidLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

def solid_logout(request):
    logout(request)
    return redirect('create_ticket')
