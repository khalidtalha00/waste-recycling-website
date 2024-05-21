from django.contrib import admin

# Register your models here.
from.models import Feedback


class AdminFeedback(admin.ModelAdmin):
    list_display = ['name','email','message']

admin.site.register(Feedback,AdminFeedback)
