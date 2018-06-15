from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^books/$',views.BooksAPIView.as_view()),
    url(r'^books/(?P<id>\d+)$',views.BookAPIView.as_view()),
]
