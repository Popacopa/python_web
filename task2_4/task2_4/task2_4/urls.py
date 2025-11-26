
from django.contrib import admin
from django.urls import path
from task2_4_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view()),
    path('addItem/<str:item>/', Form.as_view()),
    path('delete/<str:item>/<int:id>', Delete.as_view()),
    path('delete/<str:item>/<str:id>', Delete.as_view()),
    path('update/<str:item>/<int:id>', Update.as_view()),
    path('update/<str:item>/<str:id>', Update.as_view())
]
