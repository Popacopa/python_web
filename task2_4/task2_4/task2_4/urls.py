
from django.contrib import admin
from django.urls import path
from task2_4_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view())
]
