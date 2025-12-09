from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('report-issue/', views.report_issue, name='report_issue'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path("issue/<int:id>/", views.issue_detail, name="issue-detail"),
    path("issue/<int:id>/update-status/", views.update_issue_status, name="update-issue-status"),
    path("issue-success/", views.issue_success, name="issue-success")
]
