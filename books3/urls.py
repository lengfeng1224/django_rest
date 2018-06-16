from django.conf.urls import url
from . import views
from . import views_GenericAPIView

urlpatterns=[
    # url(r'^books/$',views.BookListView.as_view()),
    # url(r'^books/$',views_GenericAPIView.BookListView.as_view()),
    url(r'^books/$',views.BookListView.as_view()),
    url(r'^books/(?P<pk>\d+)/$',views.BookView.as_view())
]
