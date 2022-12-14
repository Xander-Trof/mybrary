from django.urls import path

from django.contrib.auth.views import LoginView, logout_then_login
from django.views.generic import CreateView

from book_auth_app.forms import CustomCreationForm


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='auth_app/login.html',
    ), name='login'),
    path('logout/', logout_then_login, name='logout'),

    path('register/', CreateView.as_view(
        template_name='auth_app/register.html',
        form_class=CustomCreationForm,
        success_url='/'
    ), name='register')
]
