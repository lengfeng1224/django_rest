from django.conf.urls import url
from . import views_APIView
from . import views_GenericAPIView
from . import views_GenericAPIView_mixins
from . import views_fourchildclass

# 使用视图集
from . import views_ViewSet
from . import views_ViewSet_Generic
from . import views_ViewSet_ModelView

urlpatterns=[
    # views_APIView
    # url(r'^books/$',views_APIView.BookListView.as_view()),

    # views_GenericAPIView
    # url(r'^books/$',views_GenericAPIView.BookListView.as_view()),

    # views_GenericAPIView_mixins
    # url(r'^books/$',views_GenericAPIView_mixins.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$',views_GenericAPIView_mixins.BookView.as_view())

    # views_fourchildclass
    # url(r'^books/$',views_fourchildclass.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$',views_fourchildclass.BookView.as_view())

    # Viewset
    # url(r'^books/$', views_ViewSet.BookListView.as_view({'get': 'list', 'post': 'create'})),

    # GenericViewSet
    # url(r'^books/$', views_ViewSet.BookListView.as_view({'get': 'list', 'post': 'create'})),

    # ModelViewSet
    url(r'^books/$',views_ViewSet_ModelView.BookListView.as_view({'get':'list','post':'create'})),
    url(r'^books/(?P<pk>\d+)/$',views_ViewSet_ModelView.BookView.as_view({'put':'partial_update','get':'retrieve','delete':'destroy'}))


]
