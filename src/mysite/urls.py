from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from posts import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'docs/', include_docs_urls(title='WOLF APIs')),
]

urlpatterns += router.urls
