from django.contrib import admin
from django.urls import path
from .. import student.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentAPIView.as_view()),
    path('student/<int:pk>', views.StudentAPIView.as_view()),
]
