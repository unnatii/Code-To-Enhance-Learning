from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
        url(r'^board/', views.board, name='board'),
        url(r'^tutor/', views.tutor, name='tutor'),
        url(r'^details/', views.details, name='details'),
]
