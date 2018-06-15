from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter
urlpatterns = [
]

router = DefaultRouter()
router.register(r'books',views.BookInfoViewSet)
print(router.urls)
urlpatterns+= router.urls
