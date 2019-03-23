from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('person/detail/<int:person_id>/', views.DetailView.as_view(), name='detail'),
    path('person/add/', views.AddView.as_view(), name='add'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('persons', views.PersonView.as_view(), name='persons'),
]