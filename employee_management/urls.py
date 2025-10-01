from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

class CustomLogoutView(auth_views.LogoutView):
    http_method_names = ['get', 'post']

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(next_page='login'), name='logout'),
    path('', auth_views.LoginView.as_view(template_name='login.html')),
]
