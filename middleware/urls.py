from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/', views.person, name='person'),
    path('person/<int:person_id>', views.person_update, name='person_update'),
]
