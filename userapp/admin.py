from django.contrib import admin

from userapp.models import CustomUser, IssueReport

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(IssueReport)