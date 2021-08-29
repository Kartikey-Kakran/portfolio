from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='home'),
    # path('download/', views.download_file, name='d')
    path('download/<str:filepath>/', views.download_file)
]