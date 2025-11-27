from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('report-issue/', views.report_issue, name='report_issue'),
]
