from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='Index'),
    path('pickup/',views.pickup,name='requestpickup'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('savefeedback',views.savefeedback,name='savefeedback'),
]